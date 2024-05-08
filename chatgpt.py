import g4f

def gpt_handle(query):
	response = g4f.ChatCompletion.create(
		        model=g4f.models.gpt_4,
		        provider=g4f.Provider.Bing,
		        messages=[{"role": "user", "content": f"{query}"}],
		    )
		    
	return(response)