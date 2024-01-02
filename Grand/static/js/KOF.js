import Map from "./Map.js";
import Kyo from "./roles/Kyo.js";

export default class KOF {
    constructor(id) {
        this.$id = $('#' + id)
        this.map = new Map(this)
        this.players = [new Kyo(this, {
            id: 0, x: 200, y: 0, width: 120, height: 200, color: 'blue',
        }), new Kyo(this, {id: 1, x: 900, y: 0, width: 120, height: 200, color: 'red',})]
    }
}