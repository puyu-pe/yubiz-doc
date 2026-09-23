(() => {
  const toggleSelector = ":scope > .md-nav__toggle";
  const itemSelector = ":scope > .md-nav__item--nested";

  function setExpanded(toggle, expanded) {
    toggle.checked = expanded;
    const item = toggle.closest(".md-nav__item--nested");
    const navigation = item?.querySelector(":scope > .md-nav");

    if (navigation) navigation.setAttribute("aria-expanded", String(expanded));
  }

  function closeBranch(item) {
    item.querySelectorAll(".md-nav__item--nested > .md-nav__toggle").forEach((toggle) => setExpanded(toggle, false));
  }

  function synchronize() {
    const navigation = document.querySelector(".md-sidebar--primary .md-nav--primary");
    if (!navigation) return;

    navigation.querySelectorAll(".md-nav__item--nested").forEach((item) => {
      const toggle = item.querySelector(toggleSelector);
      if (toggle) setExpanded(toggle, item.classList.contains("md-nav__item--active"));
    });

    if (navigation.dataset.sidebarAccordion) return;
    navigation.dataset.sidebarAccordion = "true";
    navigation.addEventListener("change", (event) => {
      const toggle = event.target;
      if (!(toggle instanceof HTMLInputElement) || !toggle.matches(".md-nav__toggle")) return;

      const item = toggle.parentElement;
      if (!item?.matches(".md-nav__item--nested") || !navigation.contains(item)) return;

      setExpanded(toggle, toggle.checked);
      if (!toggle.checked) return;

      item.parentElement?.querySelectorAll(itemSelector).forEach((sibling) => {
        if (sibling !== item) closeBranch(sibling);
      });
    });
  }

  document$.subscribe(synchronize);
})();
