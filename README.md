Downloads files form GAP data portal

gap-download.py samples.txt outfolder/ 8

Where samples.txt is a text file of your search terms, one term for each row. If a term hits more than one file url, all files will be downloaded. '8' is the number of threads to use for downloading file sin parallel.

https://usersupport.bioplatforms.com/find_filter_download.html

Do not use booleans with fields, only in simple text e.g. one field only: "sample_id:102.100.100/79784" or a text string: "79784 AND 81963", which gets sample 79784 library 81963 only.


https://toolkit.data.wa.gov.au/hc/en-gb/articles/4413492209935-Search-using-Solr-query-language


Search fields that can be specified:'access_control_date', 'access_control_mode', 'access_control_reason', 'analysissoftwareversion', 'author', 'author_email', 'bait_set_name', 'bait_set_reference', 'base_url', 'ccg_jira_ticket', 'creator_user_id', 'data_generated', 'data_type', 'dataset_id', 'date_data_published', 'date_of_transfer', 'date_of_transfer_to_archive', 'description', 'dna_extract', 'dna_extract_pressed_sheet', 'download', 'facility', 'family', 'flow_cell_id', 'folder_name', 'genomic_material_associated_references', 'genomic_material_preparation_date', 'genomic_material_preparation_materials', 'genomic_material_preparation_process', 'genomic_material_preparation_type', 'genomic_material_prepared_by', 'herbarium_code', 'id', 'id_vetting_by', 'isopen', 'library_construction_protocol', 'library_id', 'license_id', 'license_title', 'living_collections_catalog_number', 'living_collections_material_sample_rna', 'living_collections_record_number', 'living_collections_recorded_by', 'maintainer', 'maintainer_email', 'metadata_created', 'metadata_modified', 'nagoya_protocol_compliance', 'nagoya_protocol_permit_number', 'name', 'notes', 'num_resources', 'num_tags', 'organization', 'owner_org', 'preservation_temperature', 'preservation_type', 'private', 'project_aim', 'resource_permissions', 'sample_id', 'sample_submitter_email', 'sample_submitter_name', 'scientific_name', 'scientific_name_authorship', 'scientific_name_notes', 'sequence_data_type', 'sequencer', 'silica_gel', 'silica_gel_id', 'silica_gel_pressed_sheet', 'state', 'ticket', 'title', 'type', 'url', 'version', 'voucher_herbarium_catalog_number', 'voucher_herbarium_collector_id', 'voucher_herbarium_record_number', 'voucher_herbarium_recorded_by', 'resources', 'tags', 'groups', 'relationships_as_subject', 'relationships_as_object'
