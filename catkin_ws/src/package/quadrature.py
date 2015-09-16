#!/usr/bin/python
# Object for decoding/estimating Quadrature decodings.
# Framework by: Jason Ziglar <jpz@vt.edu>
# Update function and changes by: Thomas Schluszas <tms2874@vt.edu>

class QuadratureEstimator:
  def __init__(self, ticks_per_revolution):
    self.ticks_per_revolution = ticks_per_revolution
    self._position = 0
    self._velocity = 0
    #added self variables to initialize, for the update function
    self._a = False
    self._b = False
    self._time = 0

  def update(self, a_state, b_state, time):
    #establishes old position for later calculation
    p_old = self._position
    #establishes numerical old/new values that help determine changes in signals, set at 0 for now
    a_new = 0
    a_old = 0
    b_new = 0
    b_old = 0
      
    #changes values for the 4 variables based on current and previous states
    if a_state == True:
      a_new = 1
    if self._a == True:
      a_old = 1
    if b_state == True:
      b_new = 1
    if self._b == True:
      b_old = 1
    #determine changes in signal since last update
    a_change = a_new - a_old
    b_change = b_new - b_old
      
    #determine changes in position based on signal changes and current states. Note that position is measured in revolutions.
    if (a_change == 1 and b_state == False) or (b_change == 1 and a_state == True) or (a_change == -1 and b_state == True) or (b_change == -1 and a_state == False):
      self._position = float(self._position + 1/(4*ticks_per_revolution))
    if (b_change == 1 and a_state == False) or (a_change == 1 and b_state == True) or (b_change == -1 and a_state == True) or (a_change == -1 and b_state == False):
      self._position = float(self._position - 1/(4*ticks_per_revolution))
      
    #determines velocity based on changes in position and time
    self._velocity = float((self._position - p_old) / (time - self._time))
    #update "old" values to the current ones, for future update calls
    self._time = time
    self._a = a_state
    self._b = b_state

 
  @property
  def position(self):
      return self._position
  @property
  def velocity(self):
      return self._velocity

