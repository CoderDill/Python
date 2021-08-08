class BoggleGame {
  constructor(board, time) {
    this.time = time;
    this.board = $(board);

    $("form.enter-guess").on("submit", this.handleSubmit.bind(this));
  }

  async handleSubmit(evt) {
    evt.preventDefault();

    guess = evt.target[0].value;
    const res = await axios.get("/check-guess", { params: { guess: guess } });
    console.log(res);
  }
}
