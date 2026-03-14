window.__FOLD_SCRIPT_LOADED__ = true;
console.log("fold-post.js loaded ✅");

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll("button.fold-button");
  console.log("fold buttons found:", buttons.length);

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const post = btn.closest(".one-post");
      if (!post) return;

      post.classList.toggle("folded");

      btn.textContent = post.classList.contains("folded")
        ? "Развернуть"
        : "Свернуть";
    });
  });
});