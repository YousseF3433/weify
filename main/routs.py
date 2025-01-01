from flask import render_template, request, redirect, url_for, flash, send_from_directory, session, Response
from flask_login import login_user, current_user, logout_user
from flask_mail import Message
from sqlalchemy import desc

from . import app, db, bcrypt, mail
from .models import User, Por, Question, Blog, Buying, From, Cat


@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt') # type: ignore

@app.route("/sitemap.xml")
def sitemap():
    base_url = request.url_root.rstrip('/')
    posts = Blog.query.all()
    pages = [
        {"loc": "/", "lastmod": "2024-12-22", "priority": "1.0"},
        {"loc": "/about", "lastmod": "2024-12-20", "priority": "0.8"},
        {"loc": "/services", "lastmod": "2024-12-20", "priority": "0.8"},
        {"loc": "/portfolio", "lastmod": "2024-12-18", "priority": "0.7"},
        {"loc": "/contact", "lastmod": "2024-12-19", "priority": "0.6"},
        {"loc": "/faq", "lastmod": "2024-12-19", "priority": "0.6"},
        {"loc": "/pricing", "lastmod": "2024-12-19", "priority": "0.7"},
    ]
    for post in posts:
        pages.append({
            "loc": f"/blog/{post.id}",
            "lastmod": post.date,
            "priority": "0.5"
        })
    sitemap_xml = render_template("sitemap.xml", pages=pages, domain=base_url)
    return Response(sitemap_xml, mimetype="application/xml")

@app.before_request
def before_request():
  if request.method == "GET" and "vist-before" not in session:
    from_which_site = request.args.get("f")
    if from_which_site:
      site = From.query.filter_by(from_site=from_which_site).first()
      if site:
        site.number += 1
        db.session.commit()
        session["vist-before"] = True

@app.route("/")
@app.route("/index")
def index():
  por = Por.query.order_by(desc(Por.id)).limit(2).all()
  blogs = Blog.query.filter(Blog.index).order_by(Blog.index).limit(3).all()
  return render_template("index.html", title="Home - Webify | Leading Web Design & Development Company in Egypt",
                         des="Welcome to Webify, your go-to web development company. We specialize in custom web design, e-commerce solutions, and SEO optimization to help your business succeed online. Get started with us today!", 
                         blogs=blogs, 
                         pors=por
                        )

@app.route("/about")
def about():
  return render_template("about.html", title="About Us - Webify | Expert Web Design & Development in Egypt", des="Learn more about Webify, a leading web development company based in Egypt. We specialize in custom web design, e-commerce solutions, and SEO optimization to help businesses thrive online. Discover our story, mission, and how we can bring your vision to life.")
  
@app.route("/blogs")
def blogs():
  page = request.args.get("page", 0, type=int) * 6
  return render_template("blogs.html", title="Web Design & Development Blogs - Webify | Expert Insights & Tips", des="Browse our blogs for expert web development and design tips, trends, and best practices. Stay updated with valuable insights to help you build better websites and improve your online presence. Webify – Your partner for professional web solutions", blogs=Blog.query.all()[page: page + 10], page=page // 6)

@app.route("/blog/<int:id>")
def blog(id):
  blog = db.session.get(Blog, id)
  return render_template("blog.html", title=f"Blog - {blog.title}", des=blog.shor_description, blog=blog) # type: ignore

@app.route("/contact", methods=["GET", "POST"])
def contact():
  if request.method == "POST":
    name = request.form.get("name")
    message = request.form.get("message")
    phone = request.form.get("phone")
    company = request.form.get("company")
    budget = request.form.get("budget")
    msg = Message(
        f"{name} send this email",
        sender="youssef.ahmed.portfolio@gmail.com",
        recipients=["youssefahmedw230@gmail.com"],
        body = f"""      
        phone:  {phone}
        company: {company}
        budget: {budget}
        "
        {message}
        "
        """    
    )
    buying = Buying(phone=phone, company=company, name=name, mes=message, budget=budget)# type: ignore
    db.session.add(buying)
    db.session.commit()
    if not phone:
        msg = Message(
            f"new email has Subscribed {name}",
            sender="youssef.ahmed.portfolio@gmail.com",
            recipients=["youssefahmedw230@gmail.com"],
        )
    mail.send(msg)
    flash("email was Subscribed", "info")
    return redirect(url_for("index"))
  return render_template("contact.html", title="Contact Us - Webify | Get in Touch with Our Web Development Team",
                         des="Have questions or need a quote? Contact Webify today for expert web design and development services. We're here to help you with all your web solutions needs. Reach out and start your project with us!",
                        )

@app.route("/faq")
def faq():
   return render_template("faq.html", title="FAQ - Webify | Web Design & Development Frequently Asked Questions",
                          des="Find answers to common questions about our web design and development services. Learn more about our process, pricing, and how Webify can help bring your website vision to life.",
                          questions = Question.query.all()
                          )

@app.route("/portfolio")
def portfolio():
  return render_template("portfolio.html" , title="Portfolio - Webify | Our Web Design & Development Projects",
                         des="Explore Webify's portfolio showcasing successful web design and development projects. See how we’ve helped businesses with custom websites, e-commerce solutions, and more.",
                         pors = Por.query.all(),
                         cats = Cat.query.all())

@app.route("/pricing")
def pricing():
  mode = request.args.get("mode") 
  active = request.args.get("active")
  return render_template("pricing.html", title="Pricing - Webify | Affordable Web Design & Development Packages",
                         des="Explore Webify's transparent pricing for custom web design, development, and SEO services. Choose the perfect package to fit your needs and budget, whether you're looking for a simple website or a full-scale e-commerce solution.",
                         mode=mode,
                         active=active
                        )
  
@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
     email = request.form.get("login-email")
     password = request.form.get("login-password")
     user = User.query.filter_by(email=email).first()
     if user and bcrypt.check_password_hash(user.password, password):
       login_user(user, remember=False)
       flash("you logined successfully", "success")
       return redirect(url_for("index"))
     flash("your email or password is not correct", "danger")
  return render_template("login.html", title="login", 
                         kw="webify, webify.com, website, login, to, webify",
                         des="webify is a tech company"
                        )

@app.route("/signup", methods=["GET", "POST"])
def signup():
   if request.method == "POST":
     name = request.form.get("signup-name")
     email = request.form.get("signup-email")
     password = request.form.get("signup-password")
     hash_pass = bcrypt.generate_password_hash(password).decode("utf-8") 
     user = User(username=name, email=email, password=hash_pass) # type: ignore
     db.session.add(user)
     db.session.commit()
     login_user(user, remember=False)
     flash(f"Account created successfully for {name}", "success")
     return redirect(url_for("index"))
   return render_template("signup.html", title="signup", 
                          kw="webify, webify.com, website, signup to webify",
                          des="webify is a tech company"
                         )
  
@app.route("/logout")
def logout():
   if current_user.is_authenticated:
     logout_user()
     flash("You logout successfully!", "info")
     return redirect(url_for("index"))
   flash("You can't logout", "danger")
   return redirect(url_for("index"))

@app.route("/services")
def services():
  return render_template("services.html", title="Web Design and Development Services | E-Commerce, SEO, Hosting & More", des="Explore our professional web design, e-commerce development, SEO optimization, and reliable hosting services. We deliver customized solutions to help your business succeed online.")
  
@app.route("/form-phone", methods=["POST"])
def form_phone(): 
   phone = request.form.get("phone-footer")
   goto = request.form.get("goto")
   if phone:
      msg = Message(
          "new phone",
          sender="youssef.ahmed.portfolio@gmail.com",
          recipients=["youssefahmedw230@gmail.com"],
          body = f"""      
          phone:  {phone}
          """    
      )
      mail.send(msg)
   return redirect(url_for(f"{goto}"))