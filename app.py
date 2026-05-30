# FastAPI modules
from fastapi import FastAPI, Request, Form, Depends, HTTPException

# returning HTML pages and redirects
from fastapi.responses import HTMLResponse, RedirectResponse

# static files like CSS, JS, images
from fastapi.staticfiles import StaticFiles

# rendering HTML templates
from fastapi.templating import Jinja2Templates

# JWT token creation function
from auth.jwt_handler import sign_jwt

# JWT authentication middleware
from auth.auth_bearer import JWTBearer

# Function to validate username and password
from auth.users import check_user

# Chatbot response function
from query import get_response


# Create FastAPI application
app = FastAPI()


# Mount static folder
# Anything inside static/ can be accessed using /static
app.mount("/static", StaticFiles(directory="static"), name="static")


# Configure templates folder
templates = Jinja2Templates(directory="templates")


# =========================
# LOGIN PAGE ROUTE
# =========================

# Open login page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):

    # Render login.html
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


# =========================
# LOGIN API
# =========================

# Handle login form submission
@app.post("/login")
async def login(

    # Get username from form
    username: str = Form(...),

    # Get password from form
    password: str = Form(...)
):

    # Validate username and password
    if check_user(username, password):

        # Generate JWT token
        token = sign_jwt(username)

        # Redirect user to chatbot page
        response = RedirectResponse(
            url="/chat-ui",
            status_code=303
        )

        # Store JWT token in browser cookie
        response.set_cookie(
            key="access_token",
            value=token["access_token"],
            httponly=True
        )

        return response

    # If login fails
    raise HTTPException(
        status_code=401,
        detail="Invalid Username or Password"
    )


# =========================
# CHATBOT UI PAGE
# =========================

# Protected route
# User must have valid JWT token
@app.get("/chat-ui", response_class=HTMLResponse)
async def home(

    # Request object
    request: Request,

    # JWT validation
    token: str = Depends(JWTBearer())
):

    # Render chatbot UI
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "response": ""
        }
    )


# =========================
# CHAT API
# =========================

# Handle chatbot messages
@app.post("/chat", response_class=HTMLResponse)
async def chat(

    # Request object
    request: Request,

    # Get message from form
    message: str = Form(...),

    # JWT authentication
    token: str = Depends(JWTBearer())
):

    # Generate chatbot response
    bot_response = get_response(message)

    # Return updated chatbot UI
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "response": bot_response,
            "message": message
        }
    )