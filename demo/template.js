class Template {
    constructor(props) {

    }

    compoile (tpl) {
        // console.log(tpl);
        // tpl = tpl.split(/[\n\b]/);
        // console.log(tpl);

        // console.log(tpl);
        tpl.split()
        return;
    }

}

const tpl = `
            <a>{{name}}</a>
            {{#if x == 1}}
                <p>test if{{test}}</p>
            {{/if}}
            {{#each list}}<div>{{name}}</div>{{/each}}
        `


const tplTest = new Template();
const compileTpl = tplTest.compoile(tpl);


