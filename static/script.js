document.addEventListener("DOMContentLoaded", function () {

    // Table row animation

    const rows = document.querySelectorAll(
        "table tr:not(.heading)"
    );

    rows.forEach((row, index) => {

        row.style.opacity = "0";
        row.style.transform = "translateY(30px)";

        setTimeout(() => {

            row.style.transition = "all 0.7s ease";

            row.style.opacity = "1";

            row.style.transform = "translateY(0)";

        }, 300 + index * 120);

    });


    // Floating bubbles

    for (let i = 0; i < 15; i++) {

        const bubble = document.createElement("div");

        bubble.classList.add("bubble");

        bubble.style.left =
            Math.random() * 100 + "%";

        bubble.style.bottom = "-50px";

        bubble.style.width =
            10 + Math.random() * 25 + "px";

        bubble.style.height =
            bubble.style.width;

        bubble.style.animation =
            `float ${5 + Math.random() * 6}s linear infinite`;

        bubble.style.animationDelay =
            Math.random() * 5 + "s";

        document.body.appendChild(bubble);
    }

});
