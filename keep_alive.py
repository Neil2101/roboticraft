def keep_alive():
  from flask import Flask, render_template
  app = Flask(__name__)
  
  @app.route('/home')
  def home():
     return render_template('Home.html')
  @app.route('/amogus_sussy')
  def Amogus_sussy():
     return render_template('Amogus_sussy.html')
  @app.route('/donations')
  def Donations():
     return render_template('Donations.html')
  @app.route('/sponsors')
  def Sponsors():
     return render_template('Sponsors.html')
  @app.route('/special_thanks')
  def Special_thanks():
     return render_template('special_thanks.html')
  app.run(host="0.0.0.0", port=5000)