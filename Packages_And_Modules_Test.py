from Packages_And_Modules.planet import Planet
from Packages_And_Modules.calc import planet_mass, planet_vol

naboo = Planet('Naboo',3000,8,'Naboo System')


naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print (f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')