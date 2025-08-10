import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="CAREERSPHERE", layout="centered")

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"

def go_to(category):
    st.session_state.page = category

# Helper function to load lottie animation JSON from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Job Openings data
jobs = [
    {
        "title": "COHESITY - 2026 batch",
        "role": "Engineering Intern",
        "location": "Bangalore/Pune",
        "stipend": "INR 1 Lakh/month",
        "stipend_val": 100000,
        "eligibility": "2026 batch students with knowledge of programming and problem-solving",
        "link": "https://www.cohesity.com/company/careers/"
    },
    {
        "title": "POWERPLAY - 2024/2025/2026",
        "role": "Data Analyst Intern",
        "location": "Remote",
        "stipend": "30,000-45,000/month",
        "stipend_val": 37500,
        "eligibility": "Students from 2024-2026 with data analysis skills (Excel, SQL, Python preferred)",
        "link": "https://www.linkedin.com/jobs/search/?keywords=Powerplay%20Data%20Analyst%20Intern"
    },
    {
        "title": "MERCER ADVISORS - 2024/2025/2026/2027",
        "role": "Web Developer Intern",
        "location": "Remote",
        "stipend": "15,000-30,000/month",
        "stipend_val": 22500,
        "eligibility": "Students with web development skills (HTML, CSS, JavaScript)",
        "link": "https://www.mercer.com/careers.html"
    },
    {
        "title": "CISCO - 2025 & 2026",
        "role": "Software Engineer Intern",
        "location": "Bangalore",
        "stipend": "INR 98k/month",
        "stipend_val": 98000,
        "eligibility": "2025 & 2026 batch students pursuing Computer Science or related fields",
        "link": "https://jobs.cisco.com/jobs/internships"
    },
    {
        "title": "GOOGLE CLOUD - 2025 & 2026",
        "role": "Software Engineer",
        "location": "Bangalore",
        "stipend": "33.5 LPA to 40 LPA",
        "stipend_val": 3500000,
        "eligibility": "Strong coding skills; 2025 & 2026 batch graduates with CS background",
        "link": "https://careers.google.com/jobs/results/?q=intern"
    },
    {
        "title": "COGNIZANT - 2022/2023/2024",
        "role": "International Non Voice Process",
        "location": "Coimbatore",
        "stipend": "1.5 LPA to 4.5 LPA",
        "stipend_val": 150000,
        "eligibility": "2022-2024 graduates with good communication skills",
        "link": "https://careers.cognizant.com/internship"
    },
    # New jobs added here:
    {
        "title": "DELL Technologies - 2024/2025",
        "role": "Data Science Intern",
        "location": "Hyderabad",
        "stipend": "INR 60,000/month",
        "stipend_val": 60000,
        "eligibility": "Students with knowledge of Python, Machine Learning, and Data Analysis",
        "link": "https://jobs.dell.com/internships"
    },
    {
        "title": "TATA Consultancy Services - 2023/2024",
        "role": "Software Developer Intern",
        "location": "Multiple Cities",
        "stipend": "INR 25,000/month",
        "stipend_val": 25000,
        "eligibility": "Students with programming knowledge and problem-solving skills",
        "link": "https://www.tcs.com/careers/internships"
    },
    {
        "title": "Infosys - 2024/2025",
        "role": "Intern - AI & ML",
        "location": "Bangalore",
        "stipend": "INR 40,000/month",
        "stipend_val": 40000,
        "eligibility": "Students familiar with AI/ML concepts and Python programming",
        "link": "https://www.infosys.com/careers/internships.html"
    },
    {
        "title": "Amazon - 2025",
        "role": "SDE Intern",
        "location": "Hyderabad",
        "stipend": "INR 85,000/month",
        "stipend_val": 85000,
        "eligibility": "Strong coding skills; CS background; 2025 batch",
        "link": "https://www.amazon.jobs/en/jobs"
    },
    {
        "title": "Microsoft - 2024/2025",
        "role": "Software Engineer Intern",
        "location": "Bangalore",
        "stipend": "INR 90,000/month",
        "stipend_val": 90000,
        "eligibility": "Proficient in software development; CS or related field",
        "link": "https://careers.microsoft.com/internships"
    },
    {
        "title": "IBM - 2024/2025",
        "role": "Cloud Developer Intern",
        "location": "Hyderabad",
        "stipend": "INR 50,000/month",
        "stipend_val": 50000,
        "eligibility": "Students with cloud computing and development experience",
        "link": "https://www.ibm.com/careers/internships"
    },
    {
        "title": "Flipkart - 2024/2025",
        "role": "Product Management Intern",
        "location": "Bangalore",
        "stipend": "INR 70,000/month",
        "stipend_val": 70000,
        "eligibility": "Strong analytical skills and product interest",
        "link": "https://www.flipkartcareers.com/internships"
    },
    {
        "title": "Adobe - 2025",
        "role": "Software Engineer Intern",
        "location": "Noida",
        "stipend": "INR 90,000/month",
        "stipend_val": 90000,
        "eligibility": "CS students with good coding skills",
        "link": "https://adobe.wd1.myworkdayjobs.com/en-US/AdobeCareers"
    },
    {
        "title": "Zomato - 2024",
        "role": "Data Analyst Intern",
        "location": "Gurgaon",
        "stipend": "INR 40,000/month",
        "stipend_val": 40000,
        "eligibility": "Strong skills in SQL, Excel, and data visualization",
        "link": "https://zomato.com/careers"
    },
    {
        "title": "Paytm - 2024/2025",
        "role": "Backend Developer Intern",
        "location": "Noida",
        "stipend": "INR 60,000/month",
        "stipend_val": 60000,
        "eligibility": "Knowledge of Java, APIs, and databases",
        "link": "https://paytm.com/careers/internships"
    },
    {
        "title": "Goldman Sachs - 2024",
        "role": "Finance Intern",
        "location": "Mumbai",
        "stipend": "INR 85,000/month",
        "stipend_val": 85000,
        "eligibility": "Finance or commerce students with analytical skills",
        "link": "https://www.goldmansachs.com/careers/students/"
    },
    {
        "title": "Ola - 2024/2025",
        "role": "Mobile App Developer Intern",
        "location": "Bangalore",
        "stipend": "INR 55,000/month",
        "stipend_val": 55000,
        "eligibility": "Android or iOS development skills",
        "link": "https://ola.com/careers"
    },
    {
        "title": "Swiggy - 2024",
        "role": "Operations Analyst Intern",
        "location": "Bangalore",
        "stipend": "INR 35,000/month",
        "stipend_val": 35000,
        "eligibility": "Strong data and problem-solving skills",
        "link": "https://careers.swiggy.com/"
    },
    {
        "title": "Intel - 2024/2025",
        "role": "Hardware Engineer Intern",
        "location": "Bangalore",
        "stipend": "INR 75,000/month",
        "stipend_val": 75000,
        "eligibility": "Electronics and communication background",
        "link": "https://jobs.intel.com/"
    },
    {
        "title": "Byju's - 2024/2025",
        "role": "Content Developer Intern",
        "location": "Bangalore",
        "stipend": "INR 25,000/month",
        "stipend_val": 25000,
        "eligibility": "Education domain knowledge and content writing skills",
        "link": "https://byjus.com/careers/"
    },
]

# Freelancing Opportunities data
# Freelancing Opportunities data
freelancing = [
    {
        "title": "Python Web Developer for Ecommerce Projects",
        "details": "- Amount: $100  \n- Experience Level: Intermediate",
        "eligibility": "Intermediate knowledge of Python and web frameworks",
        "experience_level": "Intermediate",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "Marketing Specialist for SDP",
        "details": "- Duration: 1-3 months  \n- Experience Level: Intermediate",
        "eligibility": "Intermediate marketing knowledge and experience",
        "experience_level": "Intermediate",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "Graphic Designer",
        "details": "- Project Type: Logo and Branding  \n- Amount: $150  \n- Experience Level: Beginner to Intermediate",
        "eligibility": "Basic to intermediate graphic design skills",
        "experience_level": "Beginner to Intermediate",
        "link": "https://www.fiverr.com/"
    },
    {
        "title": "Content Writer for Tech Blog",
        "details": "- Amount: $50 per article  \n- Experience Level: Beginner",
        "eligibility": "Good writing skills, basic tech knowledge",
        "experience_level": "Beginner",
        "link": "https://www.freelancer.com/"
    },
    {
        "title": "Social Media Manager",
        "details": "- Duration: 3-6 months  \n- Experience Level: Intermediate",
        "eligibility": "Experience managing social media platforms",
        "experience_level": "Intermediate",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "Logo Designer",
        "details": "- Amount: $80  \n- Experience Level: Beginner",
        "eligibility": "Creative skills with Adobe Illustrator or similar",
        "experience_level": "Beginner",
        "link": "https://www.fiverr.com/"
    },
    # New freelancing gigs added here:
    {
        "title": "Mobile App Developer",
        "details": "- Amount: $300  \n- Experience Level: Intermediate to Expert",
        "eligibility": "Experience with Flutter or React Native",
        "experience_level": "Intermediate to Expert",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "SEO Specialist",
        "details": "- Duration: 2-4 months  \n- Experience Level: Intermediate",
        "eligibility": "Knowledge of SEO tools and Google Analytics",
        "experience_level": "Intermediate",
        "link": "https://www.freelancer.com/"
    },
    {
        "title": "Video Editor",
        "details": "- Amount: $200  \n- Experience Level: Beginner to Intermediate",
        "eligibility": "Basic video editing skills using Adobe Premiere or Final Cut",
        "experience_level": "Beginner to Intermediate",
        "link": "https://www.fiverr.com/"
    },
    {
        "title": "Copywriter for Advertising",
        "details": "- Amount: $100 per campaign  \n- Experience Level: Intermediate",
        "eligibility": "Strong writing and marketing skills",
        "experience_level": "Intermediate",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "UI/UX Designer",
        "details": "- Amount: $400  \n- Experience Level: Expert",
        "eligibility": "Portfolio of UI/UX projects required",
        "experience_level": "Expert",
        "link": "https://www.freelancer.com/"
    },
]

# Extend freelancing list with more entries
freelancing += [
    {
        "title": "UX Researcher",
        "details": "- Amount: $350  \n- Experience Level: Expert",
        "eligibility": "Experience conducting user research and analysis",
        "experience_level": "Expert",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "E-commerce Product Photographer",
        "details": "- Amount: $150  \n- Experience Level: Beginner to Intermediate",
        "eligibility": "Photography skills with portfolio",
        "experience_level": "Beginner to Intermediate",
        "link": "https://www.fiverr.com/"
    },
    {
        "title": "Translation Services (English to Spanish)",
        "details": "- Amount: $0.05 per word  \n- Experience Level: Intermediate",
        "eligibility": "Fluent in English and Spanish",
        "experience_level": "Intermediate",
        "link": "https://www.freelancer.com/"
    },
    {
        "title": "3D Modeling Artist",
        "details": "- Amount: $400  \n- Experience Level: Expert",
        "eligibility": "Experience with Blender or 3DS Max",
        "experience_level": "Expert",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "Email Marketing Specialist",
        "details": "- Duration: 1-2 months  \n- Experience Level: Intermediate",
        "eligibility": "Knowledge of Mailchimp or similar tools",
        "experience_level": "Intermediate",
        "link": "https://www.freelancer.com/"
    },
    {
        "title": "Voice Over Artist",
        "details": "- Amount: $100 per project  \n- Experience Level: Beginner to Intermediate",
        "eligibility": "Clear voice and recording setup",
        "experience_level": "Beginner to Intermediate",
        "link": "https://www.fiverr.com/"
    },
    {
        "title": "Mobile Game Developer",
        "details": "- Amount: $500  \n- Experience Level: Expert",
        "eligibility": "Experience in Unity or Unreal Engine",
        "experience_level": "Expert",
        "link": "https://www.upwork.com/"
    },
    {
        "title": "LinkedIn Profile Optimization",
        "details": "- Amount: $80  \n- Experience Level: Beginner to Intermediate",
        "eligibility": "Experience with LinkedIn and personal branding",
        "experience_level": "Beginner to Intermediate",
        "link": "https://www.fiverr.com/"
    },
    {
        "title": "Business Plan Writer",
        "details": "- Amount: $300  \n- Experience Level: Intermediate to Expert",
        "eligibility": "Strong writing and business knowledge",
        "experience_level": "Intermediate to Expert",
        "link": "https://www.freelancer.com/"
    },
    {
        "title": "Podcast Editor",
        "details": "- Amount: $150 per episode  \n- Experience Level: Intermediate",
        "eligibility": "Audio editing skills and software knowledge",
        "experience_level": "Intermediate",
        "link": "https://www.upwork.com/"
    },
]


# --- CSS for styling ---
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
    color: #333333;
}
h1, h2, h3 {
    color: #4B9CD3;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.listing-card {
    background-color: white;
    padding: 18px;
    margin-bottom: 18px;
    border-radius: 8px;
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
}
.listing-card h3 {
    margin-bottom: 8px;
}
.listing-card p {
    margin: 4px 0;
    font-size: 0.95rem;
}
.listing-card a {
    color: #4B9CD3;
    font-weight: 600;
    text-decoration: none;
}
.listing-card a:hover {
    text-decoration: underline;
}
.category-button {
    width: 100%;
    padding: 15px;
    font-size: 1.1rem;
    margin-bottom: 8px;
    background-color: #4B9CD3;
    color: white;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.category-button:hover {
    background-color: #3a7ac1;
}
.footer {
    color: #888;
    font-size: 0.9rem;
    padding: 12px 0;
    text-align: center;
}
/* Animated greeting style */
.animated-greeting {
    font-size: 2rem;
    font-weight: 700;
    color: #4B9CD3;
    text-align: center;
    margin-bottom: 15px;
    animation: fadeInUp 1.2s ease forwards;
    opacity: 0;
}
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# Home page with Lottie animation and attractive UI
if st.session_state.page == "home":
    st.markdown(
        """
        <div style="text-align:center; padding: 40px 0;">
            <h1 style="font-size:4rem; font-weight:bold; margin-bottom:0;">👩‍💻 CAREERSPHERE</h1>
            <p style="font-size:1.5rem; color:#6c757d; margin-top:0;">Your Gateway to Jobs, Freelancing & Career Growth</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Animated greeting just above the animation
    st.markdown(
        """
        <div class="animated-greeting">
            Welcome to <span style="color:#ff5722;">CAREERSPHERE</span> 
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Lottie animation
    lottie_url = "https://assets9.lottiefiles.com/packages/lf20_1pxqjqps.json"
    lottie_animation = load_lottie_url(lottie_url)
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, loop=True, height=250)
    
    st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

    st.markdown("""
    <div style="max-width:800px; margin:auto; text-align:center; font-size:1.1rem; color:#444; padding-top: 15px;">
    CAREERSPHERE is your all-in-one platform to explore exciting job openings, discover freelance gigs, and build your professional skills.  
    Whether you’re a student, freelancer, or job seeker, we provide curated opportunities and tips to help you thrive in your career journey.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💼 Job Openings", key="btn_job"):
            go_to("job_openings")
        st.markdown("<p style='text-align:center; color:#333;'>Explore latest internships, full-time roles & part-time jobs tailored for students and professionals.</p>", unsafe_allow_html=True)

    with col2:
        if st.button("🧑‍💻 Freelancing", key="btn_freelance"):
            go_to("freelancing")
        st.markdown("<p style='text-align:center; color:#333;'>Find freelance projects matching your skills and build a portfolio while earning.</p>", unsafe_allow_html=True)

    with col3:
        if st.button("📄 Resume & Canva Skills", key="btn_resume"):
            go_to("resume_canva")
        st.markdown("<p style='text-align:center; color:#333;'>Learn to design standout resumes and improve your career branding with Canva tips.</p>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>© 2025 CAREERSPHERE | SWECHA</div>", unsafe_allow_html=True)

# Job Openings page
elif st.session_state.page == "job_openings":
    st.header("JOB OPENINGS")
    if st.button("← Back to Categories"):
        go_home()

    # Filters
    locations = sorted(set(job['location'] for job in jobs))
    roles = sorted(set(job['role'] for job in jobs))

    stipend_ranges = {
        "All": (0, 10_000_000),
        "Below ₹50,000/month": (0, 50000),
        "₹50,000 - ₹1,00,000/month": (50000, 100000),
        "Above ₹1,00,000/month": (100000, 10_000_000),
    }

    selected_location = st.selectbox("Filter by Location", ["All"] + locations)
    selected_role = st.selectbox("Filter by Role", ["All"] + roles)
    selected_stipend = st.selectbox("Filter by Stipend Range", list(stipend_ranges.keys()))

    min_stipend, max_stipend = stipend_ranges[selected_stipend]

    filtered_jobs = []
    for job in jobs:
        location_match = (selected_location == "All" or selected_location == job['location'])
        role_match = (selected_role == "All" or selected_role == job['role'])
        stipend_match = min_stipend <= job['stipend_val'] <= max_stipend
        if location_match and role_match and stipend_match:
            filtered_jobs.append(job)

    if filtered_jobs:
        for job in filtered_jobs:
            st.markdown(f"""
            <div class="listing-card">
                <h3>{job['title']}</h3>
                <p><strong>Role:</strong> {job['role']}</p>
                <p><strong>Location:</strong> {job['location']}</p>
                <p><strong>Stipend/Salary:</strong> {job['stipend']}</p>
                <p><strong>Eligibility:</strong> {job['eligibility']}</p>
                <p><a href="{job['link']}" target="_blank">Apply here</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No job openings found for selected filters.")

# Freelancing page
elif st.session_state.page == "freelancing":
    st.header("FREELANCING")
    if st.button("← Back to Categories"):
        go_home()

    eligibility_levels = sorted(set(job['eligibility'] for job in freelancing))
    experience_levels = sorted(set(job['experience_level'] for job in freelancing))

    selected_eligibility = st.selectbox("Filter by Eligibility", ["All"] + eligibility_levels)
    selected_experience = st.selectbox("Filter by Experience Level", ["All"] + experience_levels)

    filtered_freelancing = []
    for job in freelancing:
        eligibility_match = (selected_eligibility == "All" or selected_eligibility == job['eligibility'])
        experience_match = (selected_experience == "All" or selected_experience == job['experience_level'])
        if eligibility_match and experience_match:
            filtered_freelancing.append(job)

    if filtered_freelancing:
        for job in filtered_freelancing:
            details_html = job['details'].replace('\n', '<br>')
            st.markdown(f"""
            <div class="listing-card">
                <h3>{job['title']}</h3>
                <p>{details_html}</p>
                <p><strong>Eligibility:</strong> {job['eligibility']}</p>
                <p><a href="{job['link']}" target="_blank">Apply here</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No freelancing opportunities found for selected filters.")

# Resume & Canva Skills page
elif st.session_state.page == "resume_canva":
    st.header("RESUME DESIGN & CANVA SKILLS")
    if st.button("← Back to Categories"):
        go_home()

    st.markdown("""
    ### Resume Writing Tips
    - Use a clean, easy-to-read layout.
    - Include sections like *Objective, Education, Skills, Projects, and Experience*.
    - Tailor your resume for each job application.
    - Avoid spelling errors and unnecessary details.

    ### Sample Resume Templates
    - [Canva Resume Templates](https://www.canva.com/resumes/templates/)  
    - [Google Docs Resume Templates](https://docs.google.com/document/u/0/)  

    ### Using Canva for Resumes
    - Choose a template that suits your style.
    - Use consistent fonts and colors.
    - Keep it simple and professional.

    ### Important Soft Skills to Highlight
    - Communication  
    - Teamwork  
    - Problem-solving  
    - Adaptability  

    ### Additional Tips
    - Write a concise cover letter tailored to the job.
    - Build and optimize your LinkedIn profile to match your resume.
    - Showcase your projects on GitHub or portfolio websites.
    """)

    st.markdown("---")

    st.subheader("Useful Resources & Tutorials")
    st.markdown("""
    - [How to Write a Resume That Stands Out (Video)](https://www.youtube.com/watch?v=QKnP4IL6H60)  
    - [Canva Design School: Resume Tutorials](https://www.canva.com/learn/design-school/)  
    - [Top 10 Resume Tips - Indeed Career Guide](https://www.indeed.com/career-advice/resume-samples)  
    - [LinkedIn Profile Optimization Tips](https://www.linkedin.com/pulse/how-optimize-your-linkedin-profile-get-more-views-jessie-mcclure)  
    """)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>© 2025 CAREERSPHERE | SWECHA</div>", unsafe_allow_html=True)
