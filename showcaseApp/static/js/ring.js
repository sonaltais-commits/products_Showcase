// Get data injected from Django
const projects = window.projectsData || [];
const boxWrapper = document.querySelector(".ring-3d");

if (!projects.length) {
  console.error("⚠️ No project data found!");
}

// --- Set CSS variables for rotation/perspective ---
const totalRotation = 360 / projects.length;
boxWrapper.style.setProperty("--total", `${totalRotation}deg`);
boxWrapper.style.setProperty("--projectCount", projects.length);
boxWrapper.parentElement.style.setProperty("--projectCount", projects.length);

// --- Build the tiles and insert them into the ring ---
projects.forEach((p, index) => {
  const tile = document.createElement("span");
  tile.classList.add("tile");
  tile.style.setProperty("--i", index);

  tile.innerHTML = `
    <div class="project-card">
      <div class="project-name">${p.Name}</div>
      <div class="project-grid">
        <div class="project-image">
          <img src="${p.Image}" alt="${p.Name}">
        </div>
      </div>
      <div class="project-detail">
        <div>
          <div class="project-desc">${p.Type}</div>
        </div>
        <div class="more_arrow">
            <a class="project-link" href="${p.link}">
            <div class="project-publish"><i class="fa-solid fa-angles-right"></i></div>
          </a>
        </div>
      </div>
    </div>
  `;

  boxWrapper.appendChild(tile);
});

// --- Add tilt effect on mouse move ---
const workSection = document.getElementById("work");
workSection.addEventListener("mousemove", (e) => {
  let offsetY = e.clientY - window.innerHeight / 2;
  let degree = (offsetY / (window.innerHeight / 2)) * 2;
  boxWrapper.style.rotate = `x ${degree}deg`;
});

//// --- Click tile to expand in center logic ---
//const tiles = document.querySelectorAll(".tile");
//const staticTile = document.getElementById("static-tile");
//
//tiles.forEach((tile, index) => {
//  tile.addEventListener("click", () => {
//    const alreadyClicked = tile.classList.contains("clicked");
//
//    // Reset previous selection
//    tiles.forEach(t => t.classList.remove("clicked"));
//    staticTile.classList.remove("scale");
//    staticTile.innerHTML = "";
//
//    if (!alreadyClicked) {
//      tile.classList.add("clicked");
//      staticTile.classList.add("scale");
//
//      // Create overlay + content wrapper
//      staticTile.innerHTML = `
//        <div class="tile-overlay"></div>
//        <div class="tile-content">${tile.innerHTML}</div>
//      `;
//
//      // Add close button inside tile-content
//      const tileContent = staticTile.querySelector(".tile-content");
//      tileContent.insertAdjacentHTML(
//        "afterbegin",
//        `<div class="tile-close" style="
//          position:absolute; top:10px; right:10px; cursor:pointer;
//          font-size:2rem; color:white; z-index:2;">&times;</div>`
//      );
//
//      const closeBtn = tileContent.querySelector(".tile-close");
//      closeBtn.addEventListener("click", (e) => {
//        e.stopPropagation();
//        staticTile.classList.remove("scale");
//        staticTile.innerHTML = "";
//        tile.classList.remove("clicked");
//      });
//
//      // Update more_arrow link if project has custom link
//      const projectData = projects[index];
//      if (projectData.link) {
//        const moreArrow = tileContent.querySelector(".more_arrow");
//        if (moreArrow) {
//          moreArrow.innerHTML = `
//            <a href="${projectData.link}" class="project-link"
//              style="display:flex; align-items:center; justify-content:center;
//              color:white; font-size:2rem;">
//              <i class="fa-solid fa-angles-right"></i>
//            </a>
//          `;
//        }
//      }
//
//      // --- Click overlay to close ---
//      const overlay = staticTile.querySelector(".tile-overlay");
//      overlay.addEventListener("click", () => {
//        staticTile.classList.remove("scale");
//        staticTile.innerHTML = "";
//        tile.classList.remove("clicked");
//      });
//    }
//  });
//});

// --- Direct open page on card click ---
const tiles = document.querySelectorAll(".tile");

tiles.forEach((tile, index) => {
    tile.addEventListener("click", () => {
        const project = projects[index];

        if (project.link) {
            window.location.href = project.link;
        }
    });
});