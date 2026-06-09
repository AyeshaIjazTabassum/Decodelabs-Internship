document
.getElementById("uploadForm")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const formData = new FormData(e.target);

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("results").innerHTML = `

    <div class="result-card">

        <div class="score-box">

            <h2>Career Readiness Score</h2>

            <div class="score-circle">
                ${data.score}%
            </div>

        </div>

        <h3 class="section-title">
            Current Skills
        </h3>

        ${data.current_skills.map(skill =>
            `<span class="skill found">${skill}</span>`
        ).join("")}

        <h3 class="section-title">
            Missing Skills
        </h3>

        ${data.missing_skills.map(skill =>
            `<span class="skill missing">${skill}</span>`
        ).join("")}

        <div class="grid">

            <div>

                <h3 class="section-title">
                    Learning Roadmap
                </h3>

                <div class="list-box">
                    <ul>
                        ${data.roadmap.map(item =>
                            `<li>${item}</li>`
                        ).join("")}
                    </ul>
                </div>

            </div>

            <div>

                <h3 class="section-title">
                    Recommended Projects
                </h3>

                <div class="list-box">
                    <ul>
                        ${data.projects.map(item =>
                            `<li>${item}</li>`
                        ).join("")}
                    </ul>
                </div>

            </div>

        </div>

        <h3 class="section-title">
            Certifications
        </h3>

        <div class="list-box">

            <ul>
                ${data.certifications.map(item =>
                    `<li>${item}</li>`
                ).join("")}
            </ul>

        </div>

    </div>

    `;
});