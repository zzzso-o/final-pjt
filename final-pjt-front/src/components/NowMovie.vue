<template>
<div class="container">

<!-- 
<b-carousel>
		<b-carousel-slide >
			<div v-for="(carousel, i) in carousels" :key="i">
        <div >
            <section :class="`hero is-medium is-${carousel.color}`">
                <div class="hero-body has-text-centered">
                    <h1 class="title">{{carousel.text}}</h1>
                </div>
            </section>
        </div>
			</div>
    </b-carousel-slide>
</b-carousel> -->

<!-- <template>
    <b-carousel>
        <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
            <section :class="`hero is-medium is-${carousel.color}`">
                <div class="hero-body has-text-centered">
                    <h1 class="title">{{carousel.text}}</h1>
                </div>
            </section>
        </b-carousel-item>
    </b-carousel>
</template> -->




<!-- <b-carousel id="movie-carousel">
	<b-carousel-slide v-for="movie in nowMovies" :key="movie.id" >

			<img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" class=" is-128x128">

	</b-carousel-slide>
</b-carousel> -->

<!-- <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active" v-for="movie in nowMovies" :key="movie.id">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="d-block w-30" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div> -->
<!-- "@/assets/mfb.jpg" "@/assets/meta.png" -->

	
		<div class="container">
			<h1 class="title">NOW MOVIES</h1>
			<div class="row">
				<div v-for="movie in nowMovies" :key="movie.id" class="card col-2">
					<div class="card-image">
						<figure>
							<router-link :to="{ name: 'movie', params: {movieId: movie.id} }">
								<div>
									<img class="cropped2" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" >
								</div>
							</router-link>
						</figure>
						</div>
					<div class="card-content" id="cardcontent">
						<strong>{{ movie.title }}</strong>
						<p>[{{ movie.release_date }}]</p>
					</div>
				</div>
			</div>
		</div>


	

  <!-- </div>
		<h1 class='title'>회원</h1>
	</div> -->
	</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import bModal from 'bootstrap-vue'
// import bAlert from 'bootstrap-vue'

// Vue.component('b-modal', bModal)
// Vue.component('b-alert', bAlert)
export default {

	data(){
        return {
            carousels: [
                { text: 'Slide 1', color: 'primary' },
                { text: 'Slide 2', color: 'info' },
                { text: 'Slide 3', color: 'success' },
                { text: 'Slide 4', color: 'warning' },
                { text: 'Slide 5', color: 'danger' }
            ]
        }
    },
	computed: {
		...mapGetters(['nowMovies'])
	},

	methods:{
		...mapActions(['fetchNowMovies']),
		// info(value) {
		// 	this.test = value
		// },
	},
	created(){
		this.fetchNowMovies()
	}
	
}

</script>
	
<style>
/* #cardimg{
	padding: auto;
	height:100px;
} */
#cardcontent{
	padding: 0;
	height:100px;
}
/* .caro{
	background-color: black;
	height: 500px;
}
.movie-carousel{
	height: 200px;
} */
.cropped2 {
	width: 100px; 
	height: 140px; 
	overflow: hidden;
}
	
</style>