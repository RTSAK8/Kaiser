import GameMenu from "./GameMenu.js";
import GamePlayground from "./playgrounds/Playground.js";
import Settings from "./Settings.js";

export default class Game {
    constructor(id,OS) {
        this.id = id;
        this.$game = $('#' + id);
        this.OS = OS;
        this.settings = new Settings(this);
        this.menu = new GameMenu(this);
        this.playground = new GamePlayground(this);

        this.start();
    }

    start() {
    }
}
