#!/usr/bin/env python

import json
import unicornhat as unicorn
import threading
from time import sleep
from datetime import datetime
from gpiozero import CPUTemperature

from flask import Flask, jsonify, make_response, request
from random import randint

blinkThread = None
globalRed = 0
globalGreen = 0
globalBlue = 0
globalLastCalled = None
globalLastCalledApi = None

#setup the unicorn hat
unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.5)

#get the width and height of the hardware
width, height = unicorn.get_shape()

app = Flask(__name__)

def setColor(r, g, b, brightness, speed) :
	global crntColors, globalBlue, globalGreen, globalRed
	globalRed = r
	globalGreen = g
	globalBlue = b

	if brightness != '' :
		unicorn.brightness(brightness)

	for y in range(height):
		for x in range(width):
			unicorn.set_pixel(x, y, r, g, b)
	unicorn.show()

	if speed != '' :
		sleep(speed)
		unicorn.clear()
		crntT = threading.currentThread()
		while getattr(crntT, "do_run", True) :
			for y in range(height):
				for x in range(width):
					unicorn.set_pixel(x, y, r, g, b)
			unicorn.show()
			sleep(speed)
			unicorn.clear()
			unicorn.show()
			sleep(speed)
		
def switchOn() :
	red = randint(10, 255)
	green = randint(10, 255)
	blue = randint(10, 255)
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()
	
def switchBlue() :
	red = 0
	green = 0
	blue = 250
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()
	
def switchRed() :
	red = 250
	green = 0
	blue = 0
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()
		
def switchGreen() :
	red = 0
	green = 250
	blue = 0
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()
			
def switchPink() :
	red = 255
	green = 108
	blue = 180
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, '', ''))
	blinkThread.do_run = True
	blinkThread.start()

def switchOff() :
	global blinkThread, globalBlue, globalGreen, globalRed
	globalRed = 0
	globalGreen = 0
	globalBlue = 0
	if blinkThread != None :
		blinkThread.do_run = False
	unicorn.clear()
	unicorn.off()

def setTimestamp() :
	global globalLastCalled
	globalLastCalled = datetime.now()

# API Blue
@app.route('/api/blue', methods=['GET'])
def apiBlue() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/blue'
	switchOff()
	switchBlue()
	setTimestamp()
	return jsonify({})

# API Red
@app.route('/api/red', methods=['GET'])
def apiRed() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/red'
	switchOff()
	switchRed()
	setTimestamp()
	return jsonify({})

# API Green
@app.route('/api/green', methods=['GET'])
def apiGreen() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/green'
	switchOff()
	switchGreen()
	setTimestamp()
	return jsonify({})

# API Pink
@app.route('/api/pink', methods=['GET'])
def apiPink() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/pink'
	switchOff()
	switchPink()
	setTimestamp()
	return jsonify({})

@app.route('/api/on', methods=['GET'])
def apiOn() :
	global globalLastCalledApi
	globalLastCalledApi = '/api/on'
	switchOff()
	switchOn()
	setTimestamp()
	return jsonify({})

@app.route('/api/off', methods=['GET'])
def apiOff() :
	global crntColors, globalLastCalledApi
	globalLastCalledApi = '/api/off'
	crntColors = None
	switchOff()
	setTimestamp()
	return jsonify({})

@app.route('/api/switch', methods=['POST'])
def apiSwitch() :
	global blinkThread, globalLastCalledApi
	globalLastCalledApi = '/api/switch'
	switchOff()
	content = request.json
	red = content.get('red', '')
	green = content.get('green', '')
	blue = content.get('blue', '')
	brightness = content.get('brightness', '')
	speed = content.get('speed', '')
	blinkThread = threading.Thread(target=setColor, args=(red, green, blue, brightness, speed))
	blinkThread.do_run = True
	blinkThread.start()
	setTimestamp()
	return make_response(jsonify())

@app.route('/api/status', methods=['GET'])
def apiStatus() :
	global globalBlue, globalGreen, globalRed, globalLastCalled, globalLastCalledApi
	cpu = CPUTemperature()
	return jsonify({ 'red': globalRed, 'green': globalGreen, 'blue': globalBlue, 'lastCalled': globalLastCalled, 'cpuTemp': cpu.temperature, 'lastCalledApi': globalLastCalledApi })


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)
