from expyriment import design, control, stimuli

#force windowed mode for developing and testing
control.set_develop_mode(True)

exp = design.Experiment(name="Circle")
control.initialize(exp)

# window settings
control.set_develop_mode(True)
control.defaults.window_mode = "window" #use windowed mode
control.defaults.window_size = (1200, 900) #optional size but this is ignored by macbook and doesn't do anything
control.defaults.screen_number = 0 #primary display

fixation = stimuli.FixCross()
circle = stimuli.Circle(radius=50)

# start experiment
control.start(exp, subject_id=1)

# show fixation cross
fixation.present(clear=True, update=True)
exp.clock.wait(1000)

# show circle
circle.present(clear=True, update=True)

# wait for keypress
exp.keyboard.wait()

control.end()