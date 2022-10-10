const btn = document.getElementById('btn3');
// ✅ Change button text on click
btn.addEventListener('click', function handleClick() {
  const initialText = 'Click me';
  btn.innerHTML = `<span style="background-color: salmon">Please wait...<span>`;
});

