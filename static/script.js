$('.cupcake-btn').click(getCupcakes)

async function getCupcakes() {
    const res = await axios.get('api/cupcakes')
    for (cupcake of res.data.cupcakes) {
        const $item =  `
        <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="${cupcake.image}" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">${cupcake.flavor}</h5>
          <p class="card-text">${cupcake.rating}</p>
          <p class="card-text">${cupcake.size}</p>
        </div>
      </div>
        `
        $('.cupcakes').append($item)
    }
}

$('.form-btn').click(async function(e) {
    e.preventDefault()
    let flavor = $('#flavor').val();
    let image = $('#image').val();
    let rating = $('#rating').val();
    let size = $('#size').val();

    await axios.post('api/cupcakes', data={'flavor': flavor, 'image': image, 'rating': rating, 'size': size})
    
    getCupcakes()
})