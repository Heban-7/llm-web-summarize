from fastapi import FastAPI, Query, HTTPException
from app.scraper import ScrapeTextFromURL
from app.summarizer import summarize_text

app = FastAPI(
    title="LLM Web Summarizer",
    description="A simple API to scrape a webpage and sumarize its content using LLM",
    version="1.0.0" 
)

@app.get("/summarize")
async def summarize(url: str=Query(..., description="URL of the webpage to summarize")):
    try:
        # scrape the webpage
        text = text.ScrapeTextFromURL(url)
        if not text:
            raise HTTPException(status_code=400, detail="No content foun at the webpage")
        
        # summarize the content 
        summary = summarize_text(text)
        return {
            "url":url,
            "summary":summary
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    