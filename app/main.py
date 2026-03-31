from fastapi import FastAPI
from app.routes import cart, checkout, admin

app = FastAPI()

app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(admin.router)
