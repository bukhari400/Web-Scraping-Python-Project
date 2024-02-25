from fastapi import FastAPI,requests
from pydantic import BaseModel
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from typing import Optional,Dict, List, Any
import os
from fastapi.templating import Jinja2Templates


myapp = FastAPI()

@myapp.get("/")
async def read():
    return "hello"