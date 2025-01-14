from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Templates
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Home - DevOps Hub</title>
</head>
<body>
    <h1>Welcome to DevOps Hub</h1>
    <p>Your one-stop solution for learning and exploring DevOps technologies.</p>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/technology">DevOps Technologies</a>
    </nav>
</body>
</html>
"""

about_template = """
<!DOCTYPE html>
<html>
<head>
    <title>About - DevOps Hub</title>
</head>
<body>
    <h1>About Us</h1>
    <p>DevOps Hub is a platform to explore, learn, and stay updated with the latest trends in DevOps.</p>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/technology">DevOps Technologies</a>
    </nav>
</body>
</html>
"""

technology_template = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Technologies</title>
</head>
<body>
    <h1>Future Advancements in DevOps Technologies</h1>
    <ul>
        <li><strong>AI-Driven DevOps:</strong> Integrating AI for predictive analytics and automated troubleshooting.</li>
        <li><strong>GitOps:</strong> Git as a single source of truth for CI/CD pipelines and infrastructure management.</li>
        <li><strong>Serverless Architecture:</strong> Leveraging serverless platforms to reduce infrastructure overhead.</li>
        <li><strong>Advanced Containerization:</strong> Utilizing tools like Kubernetes for orchestration and enhancing container scalability.</li>
        <li><strong>Infrastructure as Code (IaC):</strong> Enhanced tooling with Terraform, Pulumi, and Crossplane for multi-cloud management.</li>
        <li><strong>Edge Computing:</strong> Deploying workloads closer to users for low-latency applications.</li>
        <li><strong>DevSecOps:</strong> Integrating security into DevOps processes to ensure compliance and threat mitigation.</li>
        <li><strong>Continuous Everything (CI/CD/CT):</strong> A unified framework for continuous integration, delivery, and testing.</li>
    </ul>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/technology">DevOps Technologies</a>
    </nav>
</body>
</html>
"""

# Routes
@app.route("/")
def home():
    return render_template_string(home_template)

@app.route("/about")
def about():
    return render_template_string(about_template)

@app.route("/technology")
def technology():
    return render_template_string(technology_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
