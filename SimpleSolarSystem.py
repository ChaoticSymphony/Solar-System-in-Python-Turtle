# simple_solar_system.py

from solarsystem import SolarSystem, Sun, Planet

solar_system = SolarSystem(width=1400, height=800)

px = -0.0
py = -0.5
p1 = 200
p2 = 0

suns = (
    Sun(solar_system, mass = 100, position = (-115, 0), velocity = (0, 0.5)),
    Sun(solar_system, mass = 100, position = (115, 0,), velocity = (-0, -0.5)),
)

planet1 = Planet(solar_system, mass = 1, position = (p1, p2), velocity = (-px, -py))
planet2 = Planet(solar_system, mass = 1, position = (-p1, -p2), velocity = (px, py))

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()