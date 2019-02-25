const add = require('./practice');

describe('practice',function(){
    it('it wil be 30 if a=10 and b=20',function(){
        expect(add(10,20)).toEqual(30)
    })
})
