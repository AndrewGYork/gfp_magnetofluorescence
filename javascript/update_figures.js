function update_EGFP_figure() {
  var cartoon_filename = ("./figure_generation/cartoon/pngs/" + 
    document.getElementById("EGFP_figure_selection").value +".gif");
  var cartoon_image = document.getElementById("EGFP_cartoon");
  var data_filename = ("./figure_generation/EGFP_bead_figure_copy/pngs/" + 
    document.getElementById("EGFP_figure_selection").value + ".png"); 
  var data_image = document.getElementById("EGFP_data");
  cartoon_image.src = cartoon_filename;
  data_image.src    =    data_filename;
}


function update_scarlet_FMN_figure() {
  var filename = "./figure_generation/Scarlet_bead_figure/pngs/" + document.getElementById("scarlet_FMN_traces").value; 
  var image = document.getElementById("scarlet_FMN");
  image.src = filename;
}

function update_coli_figure() {
  var filename = "./figure_generation/e_coli/pngs/" + document.getElementById("coli_traces").value; 
  var image = document.getElementById("coli");
  image.src = filename;
}

function update_scarlet_beads_control_figure() {
  var filename = "./figure_generation/Scarlet_bead_figure/controls/pngs/" + document.getElementById("scarlet_beads_control_traces").value; 
  var image = document.getElementById("scarlet_beads_control");
  image.src = filename;
}

function update_scarlet_in_solution_figure() {
  var filename = "./figure_generation/Scarlet_protein/figure_repeat/pngs/" + document.getElementById("scarlet_in_solution_traces").value; 
  var image = document.getElementById("scarlet_in_solution");
  image.src = filename;
}

function update_scarlet_trp_mutants_figure() {
  var filename = "./figure_generation/Scarlet_bead_figure/trp_mutants/pngs/" + document.getElementById("scarlet_trp_mutants_traces").value; 
  var image = document.getElementById("scarlet_trp_mutants");
  image.src = filename;
}

function update_scarlet_FMN_concentration_figure() {
  var filename = "./figure_generation/Scarlet_protein/concentration/pngs/" + document.getElementById("scarlet_FMN_concentration_traces").value; 
  var image = document.getElementById("scarlet_FMN_concentration");
  image.src = filename;
}

function update_scarlet_green_power_figure() {
  var filename = "./figure_generation/Scarlet_protein/power_green/pngs/" + document.getElementById("scarlet_green_power_traces").value; 
  var image = document.getElementById("scarlet_green_power");
  image.src = filename;
}

function update_scarlet_red_power_figure() {
  var filename = "./figure_generation/Scarlet_protein/power_red/pngs/" + document.getElementById("scarlet_red_power_traces").value; 
  var image = document.getElementById("scarlet_red_power");
  image.src = filename;
}

function update_scarlet_others_figure() {
  var filename = "./figure_generation/Scarlet_protein/others/pngs/" + document.getElementById("scarlet_others_traces").value; 
  var image = document.getElementById("scarlet_others");
  image.src = filename;
}

function update_scarlet_others_figure_wst() {
  var filename = "./figure_generation/Scarlet_protein/others/pngs/" + document.getElementById("scarlet_others_traces_wst").value; 
  var image = document.getElementById("scarlet_others_wst");
  image.src = filename;
}

function update_scarlet_cartoon_figure() {
  var filename = "./figure_generation/cartoon/pngs/" + document.getElementById("scarlet_cartoon_traces").value; 
  var image = document.getElementById("scarlet_cartoon");
  image.src = filename;
}

function update_EGFP_cartoon_figure() {
  var filename = "./figure_generation/cartoon/pngs/" + document.getElementById("EGFP_cartoon_traces").value; 
  var image = document.getElementById("EGFP_cartoon");
  image.src = filename;
}


function update_EGFP_beads_control_figure() {
  var filename = "./figure_generation/EGFP_bead_figure/controls/pngs/" + document.getElementById("EGFP_beads_control_traces").value; 
  var image = document.getElementById("EGFP_beads_control");
  image.src = filename;
}

function update_EGFP_in_solution_figure() {
  var filename = "./figure_generation/EGFP_protein/figure_repeat/pngs/" + document.getElementById("EGFP_in_solution_traces").value; 
  var image = document.getElementById("EGFP_in_solution");
  image.src = filename;
}

function update_EGFP_FAD_concentration_figure() {
  var filename = "./figure_generation/EGFP_protein/concentration/pngs/" + document.getElementById("EGFP_FAD_concentration_traces").value; 
  var image = document.getElementById("EGFP_FAD_concentration");
  image.src = filename;
}

function update_EGFP_power_figure() {
  var filename = "./figure_generation/EGFP_protein/power/pngs/" + document.getElementById("EGFP_power_traces").value; 
  var image = document.getElementById("EGFP_power");
  image.src = filename;
}

function update_EGFP_others_figure() {
  var filename = "./figure_generation/EGFP_protein/others/pngs/" + document.getElementById("EGFP_others_traces").value; 
  var image = document.getElementById("EGFP_others");
  image.src = filename;
}

function update_EGFP_others_figure_an() {
  var filename = "./figure_generation/EGFP_protein/others/pngs/" + document.getElementById("EGFP_others_traces_an").value; 
  var image = document.getElementById("EGFP_others_an");
  image.src = filename;
}

function update_EGFP_others_figure_kyn() {
  var filename = "./figure_generation/EGFP_protein/others/pngs/" + document.getElementById("EGFP_others_traces_kyn").value; 
  var image = document.getElementById("EGFP_others_kyn");
  image.src = filename;
}

function update_EGFP_others_figure_wst() {
  var filename = "./figure_generation/EGFP_protein/others/pngs/" + document.getElementById("EGFP_others_traces_wst").value; 
  var image = document.getElementById("EGFP_others_wst");
  image.src = filename;
}

