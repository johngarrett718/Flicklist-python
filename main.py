import random
import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        listOfmovies = ["Batman", "Superman", "Ant Man", "Thor", "Iron Man"]
        # TODO: randomly choose one of the movies, and return it
        return random.choice(listOfmovies)


    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie2 = self.getRandomMovie()

        while movie == movie2:
            movie2 = self.getRandomMovie()

            # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        content2 = "<h1>Tomorrow's Movie</h1>"
        content2 += "<p>" + movie2 + "</p>"
        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"



        self.response.write(content)
        self.response.write(content2)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
