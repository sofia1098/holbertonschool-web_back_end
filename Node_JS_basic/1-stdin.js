function boldIs(text) {
  return text.replace(/is/g, '\x1b[1mis\x1b[0m');
}

process.stdout.write(
  boldIs('Welcome to Holberton School, what is your name?\n')
  );

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(boldIs(`Your name is: ${name}`));
});

process.stdin.on('end', () => {
  console.log(
    boldIs('This important software is now closing')
  );
});
