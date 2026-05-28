from expyriment import design, control, stimuli
from expyriment.misc.constants import K_LEFT, K_RIGHT

exp = design.Experiment(name="KeyPress")
control.set_develop_mode()
control.initialize(exp)


text = stimuli.TextLine("Find the circle: press left or right arrow")
circle = stimuli.Circle(radius=30, position = (-100,0))
square = stimuli.Rectangle(size=(50,50), position = (100,0))

text.present()
exp.clock.wait(1000)

circle.present(clear=True, update=False)
square.present(clear=False, update=True)
key, rt = exp.keyboard.wait()

if key == K_LEFT:
    feedback = stimuli.TextLine("Correct, you walk the path of the wise")
    feedback.present()
    exp.clock.wait(1000)
elif key == K_RIGHT:
    feedback = stimuli.TextLine("Incorrect, the fates do not favor this answer")
    feedback.present()
    exp.clock.wait(1000)
else:
    feedback = stimuli.TextLine("Error, a false key was struck")        
    feedback.present()
    exp.clock.wait(1000)


control.end()
