# math
import math

# robot
from body import Body

def makeProportionalHuman(height):
  root = Body('root', 0., 0., 0.)

  lfemur = Body('left femur', 0., -height * (.530 - .285), math.pi / 8., root)
  ltibia = Body('left tibia', 0., -height * (.285 - 0.039), -math.pi / 8., lfemur)
  lfoot = Body('left foot', height * 0.039, 0., 0., ltibia)

  rfemur = Body('right femur', 0., -height * (.530 - .285), 0., root)
  rtibia = Body('right tibia', 0., -height * (.285 - 0.039), 0., rfemur)
  rfoot = Body('right foot', height * 0.039, 0., 0., rtibia)

  torso = Body('torso', 0., height * (.818 - .530), 0., root)

  lhumerus = Body('left humerus', 0., -height * .186, math.pi / 8., torso)
  lradius = Body('left radius', 0., -height * .146, -math.pi / 8., lhumerus)
  lhand = Body('left hand', 0., -height * .108, 0, lradius)

  rhumerus = Body('right humerus', 0., -height * .186, -math.pi / 32., torso)
  rradius = Body('right radius', 0., -height * .146, 0., rhumerus)
  rhand = Body('right hand', 0., -height * .108, 0, rradius)

  head = Body('head', 0., height * (1. - .818), 0., torso)

  return root
