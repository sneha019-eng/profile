from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sneha Pundalik Lad | HR Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
scroll-behavior:smooth;
}

:root{
--navy:#0F172A;
--gold:#D4AF37;
--white:#ffffff;
--gray:#f8fafc;
--text:#475569;
}

body{
background:white;
color:var(--text);
}

.navbar{
background:var(--navy);
padding:20px;
position:fixed;
width:100%;
top:0;
z-index:1000;
}

.navbar ul{
display:flex;
justify-content:center;
gap:30px;
list-style:none;
}

.navbar a{
color:white;
text-decoration:none;
}

.hero{
background:linear-gradient(135deg,#0F172A,#1E293B);
color:white;
padding:140px 10% 100px;
min-height:100vh;
display:flex;
align-items:center;
justify-content:space-between;
flex-wrap:wrap;
}

.hero-text{
max-width:600px;
}

.hero h1{
font-size:4rem;
margin-bottom:20px;
}

.hero h3{
color:var(--gold);
margin-bottom:10px;
}

.hero p{
margin-bottom:25px;
}

.btn{
padding:12px 25px;
text-decoration:none;
border-radius:8px;
font-weight:600;
margin-right:10px;
display:inline-block;
}

.btn-primary{
background:var(--gold);
color:#000;
}

.btn-outline{
border:2px solid white;
color:white;
}

.profile{
width:300px;
height:300px;
border-radius:50%;
object-fit:cover;
border:5px solid var(--gold);
}

section{
padding:90px 10%;
}

.section-title{
text-align:center;
margin-bottom:50px;
}

.section-title h2{
font-size:2.4rem;
color:var(--navy);
}

.card{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0 5px 20px rgba(0,0,0,.1);
margin-bottom:20px;
}

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:20px;
}

.skills li{
margin-bottom:10px;
}

.contact{
background:#f8fafc;
}

footer{
background:var(--navy);
color:white;
text-align:center;
padding:30px;
}

@media(max-width:768px){

.hero{
text-align:center;
justify-content:center;
}

.hero h1{
font-size:2.5rem;
}

.profile{
margin-top:30px;
width:240px;
height:240px;
}

}

</style>
</head>

<body>

<nav class="navbar">
<ul>
<li><a href="#about">About</a></li>
<li><a href="#education">Education</a></li>
<li><a href="#skills">Skills</a></li>
<li><a href="#experience">Experience</a></li>
<li><a href="#projects">Projects</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
</nav>

<section class="hero">

<div class="hero-text">

<h3>Aspiring Human Resource Professional</h3>

<h1>Sneha Pundalik Lad</h1>

<p>
PGDM Human Resource student with a strong foundation in management studies,
people development, employee engagement, communication, and workplace growth.
Passionate about creating positive employee experiences and contributing
to organizational success.
</p>

<a href="/static/resume.pdf" class="btn btn-primary">
Download Resume
</a>

<a href="#contact" class="btn btn-outline">
Contact Me
</a>

</div>

<div>
<img src="/static/profile.jpg" class="profile">
</div>

</section>

<section id="about">

<div class="section-title">
<h2>About Me</h2>
</div>

<div class="card">
<p>
Currently pursuing PGDM in Human Resource Management at Sasmira's Business
School with a Bachelor of Management Studies background. Interested in
recruitment, employee engagement, workplace culture, talent development,
and organizational growth.
</p>
</div>

</section>

<section id="education">

<div class="section-title">
<h2>Education</h2>
</div>

<div class="grid">

<div class="card">
<h3>PGDM - Human Resource</h3>
<p>Sasmira's Business School</p>
<p>Pursuing</p>
</div>

<div class="card">
<h3>Bachelor of Management Studies</h3>
<p>CGPA: 7.34</p>
</div>

<div class="card">
<h3>HSC</h3>
<p>81%</p>
</div>

<div class="card">
<h3>SSC</h3>
<p>67%</p>
</div>

</div>

</section>

<section id="skills">

<div class="section-title">
<h2>Skills</h2>
</div>

<div class="grid">

<div class="card">
<h3>Professional Skills</h3>
<ul class="skills">
<li>Communication</li>
<li>Decision Making</li>
<li>Problem Solving</li>
<li>Adaptability</li>
<li>Quick Learning</li>
</ul>
</div>

<div class="card">
<h3>HR Skills</h3>
<ul class="skills">
<li>Recruitment Support</li>
<li>Training Coordination</li>
<li>Interview Assistance</li>
<li>Employee Communication</li>
</ul>
</div>

<div class="card">
<h3>Technical Skills</h3>
<ul class="skills">
<li>MS-CIT</li>
<li>Canva</li>
<li>Microsoft Office</li>
<li>Typing English-30</li>
</ul>
</div>

</div>

</section>

<section id="experience">

<div class="section-title">
<h2>Experience</h2>
</div>

<div class="card">
<h3>HR Intern</h3>
<p>True Value Marketing Services Pvt. Ltd. (Granules & Beans)</p>

<ul style="margin-top:15px;padding-left:20px;">
<li>Conducted HR policy training sessions.</li>
<li>Created employee training presentations.</li>
<li>Participated in campus recruitment and interviewing.</li>
</ul>
</div>

</section>

<section id="projects">

<div class="section-title">
<h2>Projects & Case Studies</h2>
</div>

<div class="grid">

<div class="card">
<h3>Project Placeholder</h3>
<p>Add HR project details.</p>
</div>

<div class="card">
<h3>Case Study Placeholder</h3>
<p>Add details.</p>
</div>

<div class="card">
<h3>Research Placeholder</h3>
<p>Add details.</p>
</div>

</div>

</section>

<section>

<div class="section-title">
<h2>Achievements</h2>
</div>

<div class="grid">

<div class="card">
HRIA Conclave Volunteer
</div>

<div class="card">
BMS Club Coordinator - Spontania
</div>

<div class="card">
Technical Head - Youthon Event
</div>

</div>

</section>

<section id="contact" class="contact">

<div class="section-title">
<h2>Contact</h2>
</div>

<div class="card">

<p><strong>Email:</strong> snehaplad0903@gmail.com</p>
<p><strong>Phone:</strong> 8082271971</p>
<p><strong>LinkedIn:</strong> Add Your LinkedIn URL</p>

</div>

</section>

<footer>

<h3>Sneha Pundalik Lad</h3>

<p>
Aspiring Human Resource Professional
</p>

</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)