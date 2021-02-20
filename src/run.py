import uvicorn
from server import app,run_cmd


if __name__ == '__main__':   
	# uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True, debug=True)
	# uvicorn.run(app=app)
	run_cmd()