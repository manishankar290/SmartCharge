from fastapi import FastAPI

app = FastAPI(
    title = "SmartCharge API",
    description = "EV CHarging Station Availability and Reservation System",
    version ="1.0.0"
)

@app.get("/")
def home():
    return {
        "message":"Welcome to SmartCharge",
        "status":"Application is Running"
    }
    
@app.get("/health")
def health_check():
    return {
        "status":"healthy"
    }
    


