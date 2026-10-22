<?php
//  ████  ██████  ████  █████  ██████
// ██   █ █ ██ █ ██  ██ ██  ██ █ ██ █
//   ██     ██   ██████ █████    ██
// █   ██   ██   ██  ██ ██  ██   ██
//  ████   ████  ██  ██ ██  ██  ████
?>

<?php $f=$fpfx.DIR_CLICOM.'stuff_open.php'; if(is_file($f)) @require_once($f); ?>

<!doctype html>
<html lang="<?=$__app_language_current?>">
<head>
<title><?=aconstant('APP_DOMAIN_STXT').aconstant('COLL_CHR').aconstant('STR_relateddat_act')?></title>
<meta charset="utf-8">

<?php
// ████  ██  ██ █████  ██  ██ ██████
//  ██   ███ ██ ██  ██ ██  ██ █ ██ █
//  ██   ██████ █████  ██  ██   ██
//  ██   ██ ███ ██     ██  ██   ██
// ████  ██  ██ ██      ████   ████
?>

<?php

	$can_do=true;

	$dat_cd=_ArrayGetValueFromIndex($_GET,'dat_cd'); // current data

	$genlst_main_sto_key=APP_VERSION_STXT."_{$dat_cd}"; // local storage for tbl
	$genlst_gensrh_sto_key="{$genlst_main_sto_key}_flt"; // local storage for flt
	$genlst_gensrh_frq=1000; // N ms between two searches
?>


<?php
//  ████   ████   ████
// ██  ██ ██   █ ██   █
// ██       ██     ██
// ██  ██ █   ██ █   ██
//  ████   ████   ████
?>

<style>
<?php $f=$fpfx.DIR_ROOT_CSS.'main_ROO.css.php'; if(is_file($f)) @require_once($f); ?>
<?php $f=$fpfx.DIR_CLICOM_CSS.'main_COM.css.php'; if(is_file($f)) @require_once($f); ?>
<?php $f=$fpfx.DIR_CLIAPP_CSS.'main_APP.css.php'; if(is_file($f)) @require_once($f); ?>
</style>

<script>

<?php
//  ████  ████    ████  █████   ████  ████    ████
// ██      ██    ██  ██ ██  ██ ██  ██  ██    ██   █
// ██ ███  ██    ██  ██ █████  ██████  ██      ██
// ██  ██  ██ ██ ██  ██ ██  ██ ██  ██  ██ ██ █   ██
//  ████  ██████  ████  █████  ██  ██ ██████  ████
?>

	<?php

	$dat_cd_arr=array
	(
	'anomal',
	'categexp',
	'countr',
	'currenc',
	'donor',
	'languag',
	'partner',
	'phase',
	'staff',
	'target',
	'teamlea',
	);

	$table_name_arr=array
	(
	'anomal'   =>'_anomref',
	'categexp' =>'_categexp',
	'countr'   =>'_countr',
	'currenc'  =>'_currenc',
	'donor'    =>'_donor',
	'languag'  =>'_languag',
	'partner'  =>'_partner',
	'phase'    =>'_phase',
	'staff'    =>'_staff',
	'target'   =>'_target',
	'teamlea'  =>'_teamlea',
	);

	$table_view_arr=array
	(
	'anomal'   =>'view_anomref_depy',
	'categexp' =>'view_categexp_depy',
	'countr'   =>'view_countr_depy',
	'currenc'  =>'view_currenc_depy',
	'donor'    =>'view_donor_depy',
	'languag'  =>'view_languag_depy',
	'partner'  =>'view_partner_depy',
	'phase'    =>'view_phase_depy',
	'staff'    =>'view_staff_depy',
	'target'   =>'view_target_depy',
	'teamlea'  =>'view_teamlea_depy',
	);

	if(!in_array($dat_cd,$dat_cd_arr))
	{
		$can_do=false;
	}
	else
	{
		$table_name=_ArrayGetValueFromIndex($table_name_arr,$dat_cd);
		$table_view=_ArrayGetValueFromIndex($table_view_arr,$dat_cd);
	}

	?>

	// js globals
	var gbl_gentbl; // handle
	let srh_fn=null; // continous search fn
	let srh_old_val=''; // continous search (last val)

</script>

</head>


<?php
//  ████   ████  ██  ██ ██████ ██████ ██  ██ ██████
// ██  ██ ██  ██ ███ ██ █ ██ █ ██     ███ ██ █ ██ █
// ██     ██  ██ ██████   ██   █████  ██████   ██
// ██  ██ ██  ██ ██ ███   ██   ██     ██ ███   ██
//  ████   ████  ██  ██  ████  ██████ ██  ██  ████
?>

<body class="uk-height-1-1">

<?php $f=$fpfx.DIR_CLICOM.'panel_left.php'; if(is_file($f)) @require_once($f); ?>
<?php $f=$fpfx.DIR_CLICOM.'panel_right.php'; if(is_file($f)) @require_once($f); ?>

<!-- background area -->
<div class="uk-background-default uk-padding-medium">

	<?php $f=$fpfx.DIR_CLICOM.'header_top.php'; if(is_file($f)) @require_once($f); ?>

	<!-- main area -->
	<div class="uk-background-default uk-padding-medium uk-padding-remove-horizontal">

		<?php if($__session_logged_in && $can_do) { ?>

		<div class="uk-flex uk-flex-middle uk-padding-small uk-padding-remove-horizontal list_header">

			<div class="uk-flex uk-width-1-2 uk-flex-middle uk-flex-left uk-padding-small_DIS uk-padding-remove-vertical_DIS">
				<div id="genlst_head_lb"></div>
				<div><badge_CNT id="genlst_recs_nbr_all" style="margin-left:30px;">0</badge_CNT></div>
				<div><button id="genlst_refresh_btn" class="icn_btn icn_btn_margl icn_refresh" <?=_UKTooltip(aconstant('STR_refresh_tip',false))?> ></button></div>
			</div>

			<div class="uk-flex uk-width-1-2 uk-flex-middle uk-flex-middle">
				<div class="uk-padding-small-left">
					<a href="_gets.php?<?=$__sid?>&fn=related_upd&add=1" class="uk-button uk-button-small uk-button-primary"><?=aconstant('STR_add_act',false)?></a>
				</div>
			</div>

			<div class="uk-flex uk-width-1-2 uk-flex-middle uk-flex-right">
				<div class="uk-padding-small-left">

					<div class="uk-inline uk-width-small@xs uk-width-medium@s">
						<button type="button" class="uk-form-icon" uk-icon="icon:search" id="genlst_gensrh_man_btn" aria-label="<?=aconstant('STR_search_act',false)?>" <?=_UKTooltip(aconstant('STR_gsearchval_act',false))?>></button>
						<button type="button" class="uk-form-icon uk-form-icon-flip" uk-icon="icon:close" id="genlst_gensrh_clr_btn" aria-label="<?=aconstant('STR_search_act',false)?>" <?=_UKTooltip(aconstant('STR_gsearchcan_act',false))?>></button>
						<input id="genlst_gensrh_inp" class="uk-input" type="search" placeholder="<?=aconstant('STR_field_cd_or_lb',false)?>" aria-label="<?=aconstant('STR_search_act',false)?>">
					</div>

				</div>
			</div>

		</div>


		<div class="uk-flex-top uk-grid-small" uk-grid>
			<div class="uk-width-1-1">
				<div id="gentbl" class="is-striped is-narrow_DIS" style="max-width:calc(100vw - 50px);max-height:calc(100vh - 225px);"></div>
			</div>
		</div>

		<?php } ?>

	</div>
	<!-- main area -->

</div>
<!-- background area -->



<?php

?>


<script type="text/javascript" charset="utf-8">
//──────────────────────────────────────
<?php
// █████  ██████  ████  █████  ██  ██
// ██  ██ ██     ██  ██ ██  ██ ██  ██
// █████  █████  ██████ ██  ██  ████
// ██  ██ ██     ██  ██ ██  ██   ██
// ██  ██ ██████ ██  ██ █████    ██
?>

$(document).ready(function(e)
{

	// init
	lst_init();
});
//──────────────────────────────────────

<?php
// █████   ████  ██████ ████    ████  ██████
// ██  ██ ██  ██ █ ██ █  ██    ██   █ █ ██ █
// ██  ██ ██████   ██    ██      ██     ██
// ██  ██ ██  ██   ██    ██ ██ █   ██   ██
// █████  ██  ██  ████  ██████  ████   ████
?>

//──────────────────────────────────────
$(document).on('click','#genlst_refresh_btn',function(e)
{
	genlst_refresh();
});
//──────────────────────────────────────
function lst_init()
{
	const br='<br />';

	// load gensrh
	srh_old_val=genlst_gensrh_loa();
	$('#genlst_gensrh_inp').val(srh_old_val);

	// init table
	gbl_gentbl=new Tabulator('#gentbl',
	{
		// maxHeight: "calc(100vh - 225px)", // essential alt : "calc(100vh - 200px)"
		maxHeight:'calc(100vh - 225px)',

		persistenceID:'<?=$genlst_main_sto_key?>',
		persistenceMode:true, // localdb then cookies
		persistence:
		{
			sort:true, //persist column sorting
			filter:true, //persist filters
			headerFilter:true, //persist header filters
			group:true, //persist row grouping
			page:true, //persist page
			// columns:true, //persist columns
		},
		// persistence:false,

		// layout:'fitData',
		// layout:'fitDataFill',
		// layout:'fitDataStretch',
		layout:'fitDataTable',
		// layout:'fitColumns',
		// layoutColumnsOnNewData:true,

		// data:test1_dat,
		// autoColumns:true,

		popupContainer:true,

		ajaxURL:'_posta.php?<?=$__sid?>&fn=related_lst_exe',
		ajaxParams:
		{
			db_name:'<?=$__db_name?>',
			dat_cd:'<?=$dat_cd?>',
			max_rec:250,
			// gen_srh:$('#genlst_gensrh_inp').val(),
		},
		ajaxConfig:'POST',
		ajaxContentType:'form',

		ajaxProgressiveLoad:'scroll',

		// before the ajax is called
		ajaxRequesting: function(url,params)
		{
			// $('#genlst_recs_nbr_all').removeClass('borderblinker');
			// console.log('ajaxRequesting');
			// $('#genlst_recs_nbr_all').css('animation','none');
			// $('#genlst_recs_nbr_all').outerWidth();
			$('#genlst_recs_nbr_all').addClass('borderblinker').one('animationend',function() { $(this).removeClass('borderblinker'); });

			// $('#genlst_recs_nbr_all').addClass(response.lst_recs_nbr_all);
		},

		// after the ajax has been called
		ajaxResponse:function(url,params,response)
		{
			// console.log('ajaxResponse');
			$('#genlst_recs_nbr_all').html(response.recs_nbr_all);
			$('#genlst_head_lb').html(response.head_lb);
			return(response);
		},


		sortMode:'remote',
		filterMode:'remote',
		filterDelay:200,
		allowEmpty:true,


		progressiveLoad:'scroll',
		// progressiveLoadDelay:200,
		progressiveLoadScrollMargin:300, // in px
		paginationSize:150, // in rows - remove local storage to enable
		// horiz pages
		// pagination:true,
		// paginationMode:'remote',
		// paginationSize:50, // in rows
		placeholder:'<?=aconstant('STR_none',false) ?>',

		// selectableRows:true,

		rowHeader: // checkboxes cfg
		{
			headerSort:false,
			resizable:false,
			frozen:true,
			width:50,
			headerHozAlign:'center',
			hozAlign:'center',
			formatter:'rowSelection',
			titleFormatter:'rowSelection',
			// cellClick:function(e,cell_obj)
			// {
			// 	cell_obj.getRow().toggleSelect();
			// }
		},

		initialSort:
		[
			{ column:'place', dir:'asc'},
			{ column:'cd', dir:'asc'},
			{ column:'id', dir:'asc'},
		],

		columns:
		[
			{	field:'id',
				title:'<?=aconstant('STR_id_fld',false) ?>',
				width:80,
				minWidth:80,
				maxWidth:120,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'cd',
				title:'<?=aconstant('STR_cd_fld',false) ?>',
				width:120,
				minWidth:120,
				maxWidth:160,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'lb',
				title:'<?=aconstant('STR_lb_fld',false) ?>',
				width:240,
				minWidth:240,
				maxWidth:280,
				hozAlign:'left',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'place',
				title:'<?=aconstant('STR_placeS_fld',false) ?>',
				width:80,
				minWidth:80,
				maxWidth:120,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'color',
				title:'<?=aconstant('STR_colorS_fld',false) ?>',
				width:60,
				minWidth:60,
				maxWidth:80,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:false,
				headerHozAlign:'center',
			},

			{	field:'cond',
				title:'<?=aconstant('STR_cond_fld',false) ?>',
				width:120,
				minWidth:120,
				maxWidth:160,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:false,
				headerHozAlign:'center',

				headerFilter:_Tbltr_filter_build.bind(null,'cond_flt','uk-select uk-form-xsmall uk-text-light_DIS','simple'), // simple / multiple
				headerFilterLiveFilter:false,
				headerFilterParams:
				{
					values:
					[
						{value:'1ENA',label:"<?=_cond2Label('1ENA')?>"},
						{value:'2HID',label:"<?=_cond2Label('2HID')?>"},
						{value:'3DIS',label:"<?=_cond2Label('3DIS')?>"},
					],
				},
			},

			{	field:'mission_nb',
				title:'<?=aconstant('STR_mission_nbrS2L_fld',false) ?>',
				width:120,
				minWidth:120,
				maxWidth:150,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'expend_nb',
				title:'<?=aconstant('STR_expend_nbrS2L_fld',false) ?>',
				width:120,
				minWidth:120,
				maxWidth:150,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'upd_dat_rel',
				title:'<?=aconstant('STR_upd_dateS_fld',false) ?>',
				width:110,
				minWidth:110,
				maxWidth:150,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'add_dat_rel',
				title:'<?=aconstant('STR_add_dateS_fld',false) ?>',
				width:110,
				minWidth:110,
				maxWidth:150,
				hozAlign:'center',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',
			},

			{	field:'upd_usr',
				title:'<?=aconstant('STR_upd_origin_fld',false) ?>',
				width:180,
				minWidth:180,
				maxWidth:220,
				hozAlign:'left',
				vertAlign:'middle',
				variableHeight:true,
				multiline:true,
				cssClass:'tab_cell_wrap_DIS',
				formatter:'html',
				headerSort:true,
				headerHozAlign:'center',

				headerFilter:_Tbltr_filter_build.bind(null,'upd_usr_flt','uk-select uk-form-xsmall uk-text-light_DIS','simple'), // simple / multiple
				headerFilterLiveFilter:false,
				headerFilterParams:
				{
					values:[ <?=_GetDistinctList($table_view,'lst_lv',"select distinct '' as k,upd_usr as v from {$table_view} where (upd_usr!='') order by upd_usr")?> ], // [ {label:"lb1",value:"cd1"}, {label:"lb2",value:"cd2"} ]
				},
			},
		], /* columns */

	}); /* Tabulator */

	// before the table is built
	gbl_gentbl.on('tableBuilding',function()
	{
		// console.log('tableBuilding');
		// $('#genlst_gensrh_inp').val(genlst_gensrh_loa());
		gbl_gentbl.setFilter('gen_srh','=',$('#genlst_gensrh_inp').val());
		// gbl_gentbl.replaceData('_posta.php?&fn=related_lst_exe',{'size2':150});
	});

	// after the table has finished building
	gbl_gentbl.on('tableBuilt',function()
	{
		// console.log('tableBuilt');
		// lst_genfilter_display();

		// display selected lines nbr
		const selhdr_obj=gbl_gentbl.element.querySelector('.tabulator-headers .tabulator-col:first-child .tabulator-col-title');
		if(selhdr_obj)
		{
			const nbr_obj=document.createElement('badge_SEL');
			nbr_obj.id='genlst_recs_nbr_sel';
			nbr_obj.style.marginLeft='0px';
			const div_obj=document.createElement('div');
			div_obj.style.textAlign='center';
			div_obj.appendChild(nbr_obj);
			selhdr_obj.appendChild(div_obj);
		}
		genlst_selnbr_set();

	});
	gbl_gentbl.on('rowSelectionChanged',function(data,rows)
	{
		genlst_selnbr_set();
	});

}
//──────────────────────────────────────
function genlst_selnbr_set()
{
	var sel_nb=gbl_gentbl.getSelectedRows().length;
	$('#genlst_recs_nbr_sel').html(sel_nb);
}
//──────────────────────────────────────
function genlst_refresh()
{
	// _Tbltr_refresh(gbl_gentbl);
	// Beep();
	const tbl=gbl_gentbl;

	const holder=tbl.element.querySelector('.tabulator-tableholder');
	const scrollTop=holder ? holder.scrollTop : 0;

	tbl.replaceData()
	.then(()=>
	{
		if(holder)
		{
			holder.scrollTop=scrollTop;
		}
	})
	.catch(err=>console.error('reload failed',err));
}
//──────────────────────────────────────
function genlst_gensrh_exe()
{
	const new_val=$('#genlst_gensrh_inp').val().trim();
	if(new_val!=srh_old_val)
	{
		$('#genlst_gensrh_inp').val(new_val);
		gbl_gentbl.setFilter('gen_srh','=',new_val);
		// console.log(new_val);
		// console.log(gbl_gentbl.getFilters());
		genlst_gensrh_sto(new_val);
		srh_old_val=new_val;
		genlst_refresh();
	}
}
//──────────────────────────────────────
function genlst_gensrh_loa()
{
	const gensrh=localStorage.getItem('<?=$genlst_gensrh_sto_key?>');
	// if(gensrh!==null)
	return(gensrh);
}
//──────────────────────────────────────
function genlst_gensrh_sto(val)
{
	localStorage.setItem('<?=$genlst_gensrh_sto_key?>',val);
}
//──────────────────────────────────────
$('#genlst_gensrh_man_btn').on('click',function(e)
{
	clearTimeout(srh_fn);
	genlst_gensrh_exe(); // immediate
});
//──────────────────────────────────────
$('#genlst_gensrh_inp').on('input',function(e)
{
	clearTimeout(srh_fn);
	srh_fn=setTimeout(genlst_gensrh_exe,<?=$genlst_gensrh_frq?>); // delayed
});
//──────────────────────────────────────
$(document).on('keydown',function(e)
{
	if(e.key==='Enter')
	{
		e.preventDefault(); // no default enter fn
		clearTimeout(srh_fn);
		genlst_gensrh_exe(); // immediate
	}
});
//──────────────────────────────────────
$('#genlst_gensrh_inp').on('blur',function(e)
{
	clearTimeout(srh_fn);
	srh_fn=setTimeout(genlst_gensrh_exe,<?=$genlst_gensrh_frq?>); // delayed
});
//──────────────────────────────────────
$('#genlst_gensrh_clr_btn').on('click',function(e)
{
	// const val='';
	$('#genlst_gensrh_inp').val('');
	// genlst_gensrh_sto(val);
	clearTimeout(srh_fn);
	genlst_gensrh_exe(); // immediate
});
//──────────────────────────────────────
$(document).on('keydown',function(e)
{
	if(e.metaKey && (e.key==='f' || e.key==='F')) // metaKey=cmde/winkey
	{
		setTimeout(()=>$('#genlst_gensrh_inp').focus().select(),100);
		e.preventDefault(); // no default find dialog
	}
});
</script>

<?php
// ██████ ██  ██ █████
// ██     ███ ██ ██  ██
// █████  ██████ ██  ██
// ██     ██ ███ ██  ██
// ██████ ██  ██ █████
?>

<?php $f=$fpfx.DIR_CLICOM.'stuff_close.php'; if(is_file($f)) @require_once($f); ?>

</body>
</html>