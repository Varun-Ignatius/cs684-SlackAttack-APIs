---Test error responses: Test that checks for a 404 Not Found error---

pm.test("status code id 404",()=>{
    pm.response.to.have.status(404);
});

pm.test("response includes error message",()=>{
    pm.expect(pm.response.text()).to.include('Not Found');
});
