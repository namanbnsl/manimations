from manim import *

class FirstScene(Scene):
  def construct(self):
   axes = Axes(
     x_range=[0, 5 + 1, 1],
     y_range=[0, 5 + 1, 1],
     color=GRAY,
     x_axis_config={"include_numbers": True},
     y_axis_config={"include_numbers": True}
   )

   x_vals = [0, 1, 2, 3, 4, 5]
   y_vals = [1, 3, 4, 5, 2, 4]

   points = [axes.c2p(x, y) for x, y in zip(x_vals, y_vals)]

   lines = VGroup(*[Line(points[i], points[i + 1]) for i in range(len(points) - 1)])
   lines.color = YELLOW
   dots = VGroup(*[Dot(point, radius=0.06, color=BLUE) for point in points])

   self.play(Create(axes), FadeIn(dots))
   self.wait(1)
   self.play(Create(lines))