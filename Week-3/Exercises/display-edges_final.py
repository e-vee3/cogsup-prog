from expyriment import design, control, stimuli

#force windowed mode for developing and testing
control.set_develop_mode(True)
control.defaults.window_mode = "window"
control.defaults.window_size = (1200,900)
control.defaults.screen_number = 0


## experiment
exp = design.Experiment(name="Circle")
control.initialize(exp)

fixation = stimuli.FixCross()
circle = stimuli.Circle(radius=50)

fixation.preload()
circle.preload()

# start experiment
control.start(exp, subject_id=1)

# trial
fixation.present()
exp.clock.wait(1000)

# show circle
circle.present()
exp.keyboard.wait()

control.end()