from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-test')
def run_test():
    try:
        # Initialize speedtest with secure=True for cloud compatibility
        st = speedtest.Speedtest(secure=True)
        st.get_best_server()
        
        # Perform the measurements
        download_speed = round(st.download() / 1_000_000, 2)
        upload_speed = round(st.upload() / 1_000_000, 2)
        ping_res = round(st.results.ping, 2)
        
        return jsonify({
            'download': download_speed,
            'upload': upload_speed,
            'ping': ping_res,
            'status': 'success'
        })
    except Exception as e:
        print(f"Detailed Server Error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)