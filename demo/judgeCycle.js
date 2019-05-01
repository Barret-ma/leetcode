function isCycle(obj) {
    // const keyList = [];
    const keyMap = new WeakMap();

    function findCycle(obj) {
        // if(keyList.indexOf(obj) !== -1 && typeof obj == 'object') {
        //     return true;
        // }
        // // console.log(obj);
        // keyList.push(obj);

        // for (let key in obj) {
        //     if (obj.hasOwnProperty(key) && findCycle(obj[key])) {
        //         return true;
        //     }
        // }
        // return false;
        if (keyMap.get(obj)) {
            return true;
        }

        if (typeof obj === 'object') {
            keyMap.set(obj, obj);
            for (let key in obj) {
                if (obj.hasOwnProperty(key) && findCycle(obj[key])) {
                    return true;
                }
            }
            return false;
        }
    }

    return findCycle(obj);
}

const a = {
    c: 1,
    b: {
        x: [1],
    }
}

a.b.j = a;
// const m = new WeakMap();
// m.set(a.b.j, a.b.j);

// console.log(m);

// console.log(m.get(a));
// console.log([[1]].indexOf(1));
console.log(isCycle(a));