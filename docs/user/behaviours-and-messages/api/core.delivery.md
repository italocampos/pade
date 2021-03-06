<div role="mai<div role="main">

<div id="section-intro" class="section">

## Message delivery module

This module contains the implementation of the message delivery service. If an
agent is unable to receive messages, this behaviour will postpone the message
and retry to send it, within a timeout. If the receiver is not available at the
timeout, the message is discarded.

</div>

<div class="section">

## Classes

  - `  class MessageDelivery (agent, max_wait) `
    
    <div class="desc">
    
    This class implements a default behaviour to ensure the messages
    delivery.
    
    MessageDelivery class executes the attempt to deliver a message to
    another agent. The sent messages remains in a queue until the
    max\_wait time is reached.
    
    ##### Attributes
    
      - **`queue`** : `queue.Queue`  
        The queue that saves the postponed messages.
      - **`max_wait`** : `float`  
        The max time to wait the receiver stay available.
    
    ##### Parameters
    
      - **`agent`** : `Agent`  
        The agent that executes the behaviour.
      - **`max_wait`** : `float`  
        The max time to wait the receiver stay available.
    
    </div>
    
    ##### Ancestors
    
      - pade.behaviours.types.CyclicBehaviour
      - pade.behaviours.base.BaseBehaviour
      - pade.behaviours.protocols.Behaviour
    
    ##### Methods
    
      - `  def action(self) `
        
        <div class="desc">
        
        Runs the actions of the message delivery service.
        
        </div>
    
      - `  def deliver(self, message) `
        
        <div class="desc">
        
        Puts a message in the delivery queue.
        
        This method pack the passed message in a dict. This package
        allows the message to be managed by the service with a
        timestamp.
        
        ##### Parameters
        
          - **`message`** : `ACLMessage`  
            The postponed message to be delivered.
        
        </div>

</div>

# Index

<div class="toc">

  - [Message delivery module](#message-delivery-module)

</div>

  - ### Super-module
    
      - `core`

  - ### [Classes](#classes)
    
      - #### `MessageDelivery`
        
          - `action`
          - `deliver`

</div>

Generated by [pdoc 0.8.1](https://pdoc3.github.io/pdoc).
