import pickle
import re
import web
import random




with open('neliti_dump','rb') as f:
	rows = pickle.load(f)


urls = (
	'/','index'
	)

class index:
	def GET(self):
		render = web.template.render('templates')
		outputed = list()
		random.shuffle(rows)
		count = 0
		while count <=100:
			outputed.append(rows[count])
			count += 1
		return render.viewtemplate(outputed)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()