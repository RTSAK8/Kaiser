let GAME_OBJECTS = []
export default class GameObject {
    constructor() {
        GAME_OBJECTS.push(this)
        this.timedelta = 0;
        this.flag = false;
    }

    start() {

    }

    update() {

    }

    destroy() {
        for (let gameobjectsKey in GAME_OBJECTS) {
            gameobjectsKey = parseInt(gameobjectsKey)
            if (GAME_OBJECTS[gameobjectsKey] === this) {
                GAME_OBJECTS.splice(gameobjectsKey, 1)
                return
            }
        }
    }

}
let last_timestamp;

let GAME_OBJECTS_FRAME = (timestamp) => {
    for (let obj of GAME_OBJECTS) {
        if (!obj.flag) {
            obj.start();
            obj.flag = true;
        } else {
            obj.timedelta = timestamp - last_timestamp;
            obj.update();
        }
    }
    last_timestamp = timestamp;
    requestAnimationFrame(GAME_OBJECTS_FRAME);
}

requestAnimationFrame(GAME_OBJECTS_FRAME);
