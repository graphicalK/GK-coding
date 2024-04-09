/*
 * SimpleReceiver.cpp
 *
 * Demonstrates receiving NEC IR codes with IRremote
 *
 *  This file is part of Arduino-IRremote https://github.com/Arduino-IRremote/Arduino-IRremote.
 *
 ************************************************************************************
 * MIT License
 *
 * Copyright (c) 2020-2023 Armin Joachimsmeyer
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is furnished
 * to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 ************************************************************************************
 */

/*
 * Specify which protocol(s) should be used for decoding.
 * If no protocol is defined, all protocols (except Bang&Olufsen) are active.
 * This must be done before the #include <IRremote.hpp>
 */
//#define DECODE_DENON        // Includes Sharp
//#define DECODE_JVC
//#define DECODE_KASEIKYO
//#define DECODE_PANASONIC    // alias for DECODE_KASEIKYO
//#define DECODE_LG
#define DECODE_NEC          // Includes Apple and Onkyo
//#define DECODE_SAMSUNG
//#define DECODE_SONY
//#define DECODE_RC5
//#define DECODE_RC6

//#define DECODE_BOSEWAVE
//#define DECODE_LEGO_PF
//#define DECODE_MAGIQUEST
//#define DECODE_WHYNTER
//#define DECODE_FAST

//#define DECODE_DISTANCE_WIDTH // Universal decoder for pulse distance width protocols
//#define DECODE_HASH         // special decoder for all protocols

//#define DECODE_BEO          // This protocol must always be enabled manually, i.e. it is NOT enabled if no protocol is defined. It prevents decoding of SONY!

//#define DEBUG               // Activate this for lots of lovely debug output from the decoders.

//#define RAW_BUFFER_LENGTH  180  // Default is 112 if DECODE_MAGIQUEST is enabled, otherwise 100.
//_________________________________________________________________________________________________________________________________________________
//V2 of battle bot movement 
//Motor Controller Pins: 8, 9, 10, 11 (parallel wires going from arduino to motor controller)
//LED Signal Pins: 7, 6, 5 (Blue, Green, and Red Respectively)
//Modified by Alexander Tran, Original code from IRRemote Library creator

//an old remote, arduino, scrap parts, and a dream
//_________________________________________________________________________________________________________________________________________________
#include <Arduino.h>

/*
 * This include defines the actual pin number for pins like IR_RECEIVE_PIN, IR_SEND_PIN for many different boards and architectures
 */
#include "PinDefinitionsAndMore.h"
#include <IRremote.hpp> // include the library


//declare movement variables
  int movement = 0;
  int weapon = 0;

void setup() {

  //declare pins
  pinMode(8,OUTPUT); //right motor backwards
  pinMode(9,OUTPUT); //right motor forwards
  pinMode(10,OUTPUT); //left motor backwards
  pinMode(11,OUTPUT); //left motor forwards

  pinMode(5,OUTPUT); //Red anode RGB LED
  pinMode(6,OUTPUT); //Green anode RGB LED
  pinMode(7,OUTPUT); //Blue anode RGB LED

    Serial.begin(115200);
    // Just to know which program is running on my Arduino
    Serial.println(F("START " __FILE__ " from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));

    // Start the receiver and if not 3. parameter specified, take LED_BUILTIN pin from the internal boards definition as default feedback LED
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);

    Serial.print(F("Ready to receive IR signals of protocols: "));
    printActiveIRProtocols(&Serial);
    Serial.println(F("at pin " STR(IR_RECEIVE_PIN)));
}

//create movement functions
void forwards() {
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  //RGB LED (red)
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(7,LOW);
}

void backwards(){
  digitalWrite(8,HIGH);
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  //RGB LED (blue)
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  digitalWrite(7,HIGH);
}

void left () {
  digitalWrite(8,LOW); //actual movement
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  //RGB LED (green)
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(7,LOW);
}

void right(){
  digitalWrite(8,HIGH);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  //RGB LED (yellow)
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,LOW);
}

void stop(){
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  //RGB LED
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  digitalWrite(7,LOW);
}

void loop() {

    /*
     * Check if received data is available and if yes, try to decode it.
     * Decoded result is in the IrReceiver.decodedIRData structure.
     *
     * E.g. command is in IrReceiver.decodedIRData.command
     * address is in command is in IrReceiver.decodedIRData.address
     * and up to 32 bit raw data in IrReceiver.decodedIRData.decodedRawData
     */
    if (IrReceiver.decode()) {

        /*
         * Print a short summary of received data
         */
        IrReceiver.printIRResultShort(&Serial);
        IrReceiver.printIRSendUsage(&Serial);
        if (IrReceiver.decodedIRData.protocol == UNKNOWN) {
            Serial.println(F("Received noise or an unknown (or not yet enabled) protocol"));
            // We have an unknown protocol here, print more info
            IrReceiver.printIRResultRawFormatted(&Serial, true);
        }
        Serial.println();

        /*
         * !!!Important!!! Enable receiving of the next value,
         * since receiving has stopped after the end of the current received data packet.
         */
        IrReceiver.resume(); // Enable receiving of the next value

        /*
         * Finally, check the received data and perform actions according to the received command
         */
        if (IrReceiver.decodedIRData.command == 0xC) { //Drive Forwards
            if (movement != 1){ //Check if the movement command is not active (aka stationary)
              movement = 1; 
            } else if (movement == 1){ //if the movement command is active (moving), then stop it when the button is pressed
                movement = 0;
            }
        } else if (IrReceiver.decodedIRData.command == 0x11) { //Drive Backwards
            if (movement != 2){
              movement = 2;
            } else if (movement == 2){
                movement = 0;
            }
        } else if(IrReceiver.decodedIRData.command == 0x19) { //Drive Left
            if (movement != 3){
              movement = 3;
            } else if (turnLeft == 3){
                movement = 0;
            }
        } else if(IrReceiver.decodedIRData.command == 0x10) { //Drive Right
            if (turnRight != 4){
              movement = 4;
            } else if (turnRight == 4){
                movement = 0;
            }
        } else if(IrReceiver.decodedIRData.command == 0x13) { //Reset Everything
            //Reset states
            movement = 0;
            weapon = 0;
            //Reset LED
            stop();
        }

        //insert movement code
        //SO OPTIMIZED!!!!!!!!!
        //no it isnt dumby
          if (movement == 1){
            forwards();
          } else if (movement == 2) {
              backwards();
          } else if (movement == 3) {
              left();
          } else if (movement == 4) {
              right();
          } else if (movement == 0) {
              stop();
          }

    }
}
      

