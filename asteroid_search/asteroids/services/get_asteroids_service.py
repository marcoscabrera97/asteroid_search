from asteroids.models import AsteroidRegistration

class GetAsteroidsService(object):
    '''
    Get asteroid registration save in the database'''
    def get_asteroids(self, width, height):
        return AsteroidRegistration.objects.filter(height=height, width=width)