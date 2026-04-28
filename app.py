from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-test')
def run_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        # Performance results
        ping = round(st.results.ping, 2)
        download = round(st.download() / 1_000_000, 2) # Convert to Mbps
        upload = round(st.upload() / 1_000_000, 2)     # Convert to Mbps
        
        return jsonify({
            'ping': ping,
            'download': download,
            'upload': upload,
            'jitter': round(st.results.client['lat'], 2) # Estimation
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)