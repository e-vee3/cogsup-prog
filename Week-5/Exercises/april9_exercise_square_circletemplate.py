from expyriment import design, control, stimuli, misc

### this is a minimal examply using expyriment for an experiment ###

#create an experiment object using "exp"

exp = design.Experiment(name= "First Experiment")

### avoid full screen mode and use a small window for development
control.set_develop_mode()

#initialize the experiment (this creates the window and prepares everything)
control.initialize(exp)

#define some constant for the experiment
STIMSIZE = 100 #size of the stimuli in pixels
GREY = misc.constants.C_GREY #a grey color for the stimulus
LATERAL_OFFSET = 200 #offset for lateral positioning

#prepare some stimuli
square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour=GREY, position=(-LATERAL_OFFSET, 0))
circle = stimuli.Circle(radius=STIMSIZE // 2, colour=GREY, position=(LATERAL_OFFSET, 0))

#preload the stimuli (this can help reduce delays during the experiment)
square.preload()
circle.preload()

#start the experiment (this will show the window and wait for a key press to start)
control.start()

#present square and circle stimuli
square.present(clear=True, update=False) #present the square without clearing the screen
circle.present(clear=False, update=True) # present the circle on top of the square

exp.clock.wait(2000) #wait 2 seconds to let the participant see the stimuli

#exit the experiment (this will close the window and clean up)
control.end()