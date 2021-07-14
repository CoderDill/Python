class BoggleGame {
  constructor(board, time) {
    this.time = time;
    this.board = $(board);

    $(".enter-guess", this.board).on("submit", this.handleSubmit.bind(this));
  }

  async handleSubmit(evt) {
    evt.preventDefault();
    const $guess = $(".guess", this.board);
    guess = $guess.val();
    const res = await axios.get("/check-guess", { params: { guess: guess } });
    console.log(res);
  }
}
