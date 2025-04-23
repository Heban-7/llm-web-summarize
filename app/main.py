from fastapi import FastAPI, Query, HTTPException
from app.scraper import Website
from app.summarizer import Summarize

app = FastAPI(
    title="LLM Web Summarizer",
    description="A simple API to scrape a webpage and sumarize its content using LLM",
    version="1.0.0" 
)

@app.get("/summarize")
async def summarize(url: str=Query(..., description="URL of the webpage to summarize")):
    try:
        # scrape the webpage
        website = Website(url)
        web_title, web_text = website.title, website.text
        if not web_text:
            raise HTTPException(status_code=400, detail="No content foun at the webpage")
        
        # summarize the content 
        summary = Summarize(website)
        return {
            "url":url,
            "summary":summary.summarize_using_ollama()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    