import cloudconvert

def cloud_convert(page_range,path):
	api = cloudconvert.Api('jJihZWVlAY2YoYnSmSOvHIADAt8BXI0G6jwb1DLKzJKIVIodL7qqWrMXoQ8SVDBy')
	process = api.convert({
    	'inputformat': 'pdf',
    	'outputformat': 'jpg',
    	'converteroptions': {
        	'page_range': page_range#'7-10'
    	},
    	'input': 'upload',
    	'file': open(path, 'rb')
	})
	process.wait() 
	process.download("/home/san/aaa")

cloud_convert('1-3', '/home/san/aaa/maths.pdf')