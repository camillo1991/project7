import { d as t, _ as a, o as _, k as c, x as n, y as p, l as e, I as o } from "./index.c2b66f9d.js";
import { _ as r } from "./text_logo.b8d7d921.js";

const d = t({}), i = "/botQR.png";

// Изменяем структуру компонента, чтобы он не ограничивал доступ только для Telegram
const l = s => (n("data-v-d257bb5e"), s = s(), p(), s),
    m = { class: "container" },
    // Изменяем текст на приветственное сообщение вместо информации о Telegram
    b = l(() => e("div", { class: "start_taurus" }, [
        e("img", { src: r }),
        e("img", { src: i }),
        e("p", null, [o("Welcome to Betaurus!")])  // Изменено сообщение
    ], -1));

const u = [b];

function f(s, h, v, x, g, y) {
    return _(), c("div", m, u);
}

const $ = a(d, [["render", f], ["__scopeId", "data-v-d257bb5e"]]);

export { $ as default };
